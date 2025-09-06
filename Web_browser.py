#!/usr/bin/env python3
import threading
import urllib.parse
import urllib.request
import sys
import io
import time

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import socketserver

import tkinter as tk
from tkinter import ttk, messagebox

# Try to use tkhtmlview (optional, for simple HTML rendering)
# pip install tkhtmlview
try:
    from tkhtmlview import HTMLScrolledText  # or HTMLLabel, HTMLScrolledText
    HAS_TKHTMLVIEW = True
except Exception:
    HAS_TKHTMLVIEW = False


# =========================
# 1) Local HTTP proxy server
# =========================

HOST = "127.0.0.1"
PORT = 7787

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122 Safari/537.36"
)

class FetchProxyHandler(BaseHTTPRequestHandler):
    """
    Simple proxy-like endpoint:
      GET /fetch?url=<percent-encoded-URL>
    - Fetches the given http/https URL using urllib
    - Returns the original content with the remote Content-Type if available
    """

    def log_message(self, fmt, *args):
        # Quieter logs
        sys.stderr.write("[%s] %s\n" % (self.address_string(), fmt % args))

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != "/fetch":
            self.send_error(404, "Use /fetch?url=<http(s) URL>")
            return

        qs = urllib.parse.parse_qs(parsed.query)
        url = (qs.get("url") or [None])[0]
        if not url:
            self.send_error(400, "Missing url parameter")
            return

        # Basic safety: only allow http/https
        if not (url.startswith("http://") or url.startswith("https://")):
            self.send_error(400, "Only http/https URLs are allowed")
            return

        # Fetch the remote content
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                content_type = resp.headers.get("Content-Type", "application/octet-stream")

            # Return response
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        except Exception as e:
            self.send_response(502)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"Proxy fetch failed: {e}".encode("utf-8"))


def start_proxy_server():
    server = ThreadingHTTPServer((HOST, PORT), FetchProxyHandler)
    # Run forever on a daemon thread
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    return server


# =========================
# 2) Tkinter "Mini Browser"
# =========================

class MiniBrowser(tk.Tk):
    def __init__(self, proxy_base):
        super().__init__()
        self.title("Mini Browser (Tkinter) – via Local Proxy")
        self.geometry("1000x700")

        self.proxy_base = proxy_base  # e.g., "http://127.0.0.1:7787/fetch?url="

        self.history = []
        self.future = []

        self._build_ui()

    def _build_ui(self):
        # Top bar: Back, Forward, URL entry, Go
        top = ttk.Frame(self)
        top.pack(side=tk.TOP, fill=tk.X, padx=8, pady=8)

        self.back_btn = ttk.Button(top, text="← Back", command=self.go_back, width=8)
        self.back_btn.pack(side=tk.LEFT, padx=(0, 5))

        self.forward_btn = ttk.Button(top, text="Forward →", command=self.go_forward, width=10)
        self.forward_btn.pack(side=tk.LEFT, padx=(0, 5))

        self.url_var = tk.StringVar()
        self.url_entry = ttk.Entry(top, textvariable=self.url_var)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 5))
        self.url_entry.bind("<Return>", lambda e: self.navigate())

        self.go_btn = ttk.Button(top, text="Go", command=self.navigate, width=6)
        self.go_btn.pack(side=tk.LEFT)

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status = ttk.Label(self, textvariable=self.status_var, anchor="w")
        status.pack(side=tk.BOTTOM, fill=tk.X)

        # Content area
        if HAS_TKHTMLVIEW:
            self.viewer = HTMLScrolledText(self, html="<h3>Welcome!</h3><p>Enter a URL above.</p>")
            self.viewer.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
        else:
            # Fallback: show plain text / HTML source
            wrap = ttk.Frame(self)
            wrap.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
            self.text = tk.Text(wrap)
            self.text.pack(fill=tk.BOTH, expand=True)
            self.text.insert("1.0", "tkhtmlview not installed.\nShowing HTML source.\n\nEnter a URL above.\n")

        # Initial button states
        self._update_nav_buttons()

    def set_status(self, text):
        self.status_var.set(text)
        self.update_idletasks()

    def normalize_url(self, url):
        url = url.strip()
        if not url:
            return ""
        # If user typed example.com, add https://
        if "://" not in url:
            url = "https://" + url
        return url

    def navigate(self):
        url = self.normalize_url(self.url_var.get())
        if not url:
            return

        # Push current into history (if any)
        if self.history and self.history[-1] != url:
            # Clear forward stack on new navigation
            self.future.clear()

        self._load_via_proxy(url)
        # Record new URL in history (only if successful load)
        if not self.history or self.history[-1] != url:
            self.history.append(url)
        self._update_nav_buttons()

    def go_back(self):
        if len(self.history) < 2:
            return
        # Move current to future, go to previous
        current = self.history.pop()
        self.future.append(current)
        url = self.history[-1]
        self._load_via_proxy(url)
        self._update_nav_buttons()
        self.url_var.set(url)

    def go_forward(self):
        if not self.future:
            return
        url = self.future.pop()
        self.history.append(url)
        self._load_via_proxy(url)
        self._update_nav_buttons()
        self.url_var.set(url)

    def _update_nav_buttons(self):
        self.back_btn.config(state=(tk.NORMAL if len(self.history) > 1 else tk.DISABLED))
        self.forward_btn.config(state=(tk.NORMAL if len(self.future) > 0 else tk.DISABLED))

    def _load_via_proxy(self, target_url):
        """
        Fetch target_url THROUGH the local proxy: /fetch?url=<target_url>
        """
        self.set_status(f"Loading: {target_url} (via proxy)")
        self.update()

        try:
            proxy_url = f"{self.proxy_base}{urllib.parse.quote(target_url, safe='')}"
            req = urllib.request.Request(proxy_url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=20) as resp:
                content_type = resp.headers.get("Content-Type", "")
                raw = resp.read()

            # Render
            if "text/html" in content_type.lower():
                # Decode charset if provided
                charset = "utf-8"
                parts = [p.strip() for p in content_type.split(";")]
                for p in parts:
                    if p.lower().startswith("charset="):
                        charset = p.split("=", 1)[1].strip()
                        break

                html = raw.decode(charset, errors="replace")

                if HAS_TKHTMLVIEW:
                    self.viewer.set_html(html)  # basic HTML support (no JS/CSS)
                else:
                    self.text.delete("1.0", tk.END)
                    self.text.insert("1.0", html)
            else:
                # Non-HTML: show basic info and (if text/*) preview content
                if HAS_TKHTMLVIEW:
                    preview = ""
                    try:
                        if content_type.startswith("text/"):
                            preview = raw.decode("utf-8", errors="replace")
                            if len(preview) > 5000:
                                preview = preview[:5000] + "\n…(truncated)…"
                    except Exception:
                        pass
                    safe_ct = content_type or "application/octet-stream"
                    self.viewer.set_html(
                        f"<h3>Downloaded non-HTML content</h3>"
                        f"<p><b>Content-Type:</b> {safe_ct}</p>"
                        f"<p>Size: {len(raw)} bytes</p>"
                        + (f"<hr><pre>{html_escape(preview)}</pre>" if preview else "")
                    )
                else:
                    self.text.delete("1.0", tk.END)
                    info = f"Downloaded non-HTML content\nContent-Type: {content_type}\nSize: {len(raw)} bytes\n"
                    # Try to show text preview
                    if content_type.startswith("text/"):
                        try:
                            preview = raw.decode("utf-8", errors="replace")
                            if len(preview) > 8000:
                                preview = preview[:8000] + "\n…(truncated)…"
                            info += "\n----- Preview -----\n" + preview
                        except Exception:
                            pass
                    self.text.insert("1.0", info)

            self.set_status(f"Loaded: {target_url}")
        except Exception as e:
            self.set_status("Error")
            if HAS_TKHTMLVIEW:
                self.viewer.set_html(
                    f"<h3 style='color:#b00'>Load error</h3><pre>{html_escape(str(e))}</pre>"
                )
            else:
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", f"Load error:\n{e}")

def html_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
         .replace("<", "&lt;")
         .replace(">", "&gt;")
         .replace('"', "&quot;")
         .replace("'", "&#39;")
    )


def main():
    # 1) Start local proxy server
    server = start_proxy_server()
    proxy_base = f"http://{HOST}:{PORT}/fetch?url="

    # 2) Launch Tkinter mini browser
    app = MiniBrowser(proxy_base)
    app.url_var.set("https://example.com")
    app.protocol("WM_DELETE_WINDOW", app.destroy)
    try:
        app.mainloop()
    finally:
        # Clean shutdown of proxy
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
