import os
import webbrowser
from typing import List, Dict
from urllib.parse import urlparse


class FontURLManager:
    def __init__(self):
        self.chrome_path = self._get_chrome_path()
        self.font_sources: Dict[str, List[str]] = {
            "Adobe Fonts": [],
            "Google Fonts": [],
            "DaFont": [],
            "MyFonts": [],
            "Envato": [],
            "Other": [],
        }

    def _get_chrome_path(self) -> str:
        """Get the Chrome path based on OS"""
        if sys.platform == "darwin":  # macOS
            return 'open -a "Google Chrome"'
        elif sys.platform.startswith("win"):  # Windows
            return "start chrome"
        else:  # Linux
            return "google-chrome"

    def clean_url(self, url: str) -> str:
        """Clean URL by removing asterisks and whitespace"""
        return url.replace("*", "").strip()

    def categorize_url(self, url: str) -> None:
        """Categorize URL by font provider"""
        url = self.clean_url(url)
        if not url:
            return

        if "fonts.adobe.com" in url:
            self.font_sources["Adobe Fonts"].append(url)
        elif "fonts.google.com" in url:
            self.font_sources["Google Fonts"].append(url)
        elif "dafont.com" in url:
            self.font_sources["DaFont"].append(url)
        elif "myfonts.com" in url:
            self.font_sources["MyFonts"].append(url)
        elif "elements.envato.com" in url:
            self.font_sources["Envato"].append(url)
        else:
            self.font_sources["Other"].append(url)

    def open_urls_in_chrome(self) -> None:
        """Open URLs in Chrome, grouped by provider"""
        total_urls = sum(len(urls) for urls in self.font_sources.values())

        print("\n📂 Opening URLs in Chrome...")
        print("=" * 50)
        print("⚠️  Please allow pop-ups in Chrome if prompted")
        print(f"🔗 Total URLs to open: {total_urls}\n")

        for provider, urls in self.font_sources.items():
            if not urls:
                continue

            print(f"\n📁 {provider} ({len(urls)} fonts):")
            for url in urls:
                print(f"  • Opening: {url}")
                try:
                    # Open URL in a new tab
                    webbrowser.open_new_tab(url)
                except Exception as e:
                    print(f"    ❌ Error opening {url}: {e}")

            if urls:  # If we opened any URLs for this provider
                input("\n⏸️  Press Enter when you've downloaded these fonts...")

        print("\n✅ All URLs have been opened!")
        print("\n📝 Next steps:")
        print("1. Download each font from the opened tabs")
        print("2. Place the downloaded files in: ~/Library/Fonts/")
        print("3. Restart any applications where you want to use the new fonts")


def main():
    print("🎨 Font Download Assistant")
    print("=" * 50)
    print("Enter font URLs (one per line)")
    print("When finished, press Enter twice\n")
    print("Supported sources:")
    print("  • Adobe Fonts (fonts.adobe.com)")
    print("  • Google Fonts (fonts.google.com)")
    print("  • DaFont (dafont.com)")
    print("  • MyFonts (myfonts.com)")
    print("  • Envato Elements (elements.envato.com)")
    print("=" * 50)

    urls = []
    while True:
        try:
            line = input().strip()
            if not line and urls:  # Empty line after some URLs
                break
            if line:
                urls.append(line)
        except EOFError:
            break

    if not urls:
        print("❌ No URLs provided. Exiting.")
        return

    manager = FontURLManager()

    # Categorize URLs
    for url in urls:
        manager.categorize_url(url)

    # Print summary before opening
    print("\n📊 URL Summary:")
    for provider, provider_urls in manager.font_sources.items():
        if provider_urls:
            print(f"  • {provider}: {len(provider_urls)} fonts")

    # Confirm before opening browsers
    response = input("\n⚠️  Ready to open URLs in Chrome? (y/n): ")
    if response.lower() != "y":
        print("❌ Operation cancelled")
        return

    # Open URLs in Chrome
    manager.open_urls_in_chrome()


if __name__ == "__main__":
    import sys

    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
