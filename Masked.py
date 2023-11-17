import pyshorteners
from urllib.parse import urlparse

class URLMaskingTool:
    def __init__(self, creator_name, creator_instagram, additional_text):
        self.s = pyshorteners.Shortener()
        self.creator_name = creator_name
        self.creator_nam = creator_nam
        self.creator_instagram = creator_instagram
        self.additional_text = additional_text

    def print_banner(self):
        banner = r''' 
 __  __   ______  ____    __      __  ______  ____    ____      
/\ \/\ \ /\  _  \/\  _`\ /\ \  __/\ \/\  _  \/\  _`\ /\  _`\    
\ \ \/'/'\ \ \L\ \ \ \L\ \ \ \/\ \ \ \ \ \L\ \ \ \L\ \ \ \L\_\  
 \ \ , <  \ \  __ \ \ ,  /\ \ \ \ \ \ \ \  __ \ \ ,  /\ \  _\L  
  \ \ \\`\ \ \ \/\ \ \ \\ \\ \ \_/ \_\ \ \ \/\ \ \ \\ \\ \ \L\ \
   \ \_\ \_\\ \_\ \_\ \_\ \_\ `\___x___/\ \_\ \_\ \_\ \_\ \____/
    \/_/\/_/ \/_/\/_/\/_/\/ /'\/__//__/  \/_/\/_/\/_/\/ /\/___/ 
                                                                
                                                                
                          Created By KARWARE                  
        '''
        
        print(banner)

    def mask_url(self, original_url, custom_domain, phishing_keywords):
        short_url = self.s.tinyurl.short(original_url)
        parsed_url = urlparse(short_url)
        formatted_keywords = "-".join(phishing_keywords.split())
        masked_url = f"{parsed_url.scheme}://{custom_domain}-{formatted_keywords}@{parsed_url.netloc}{parsed_url.path}"
        return masked_url

    def get_user_input(self):
        original_url = input("Enter the original link: ")
        custom_domain = input("Enter your custom domain: ")
        phishing_keywords = input("Enter phishing keywords (separated by commas): ")
        return original_url, custom_domain, phishing_keywords

    def run(self):
        print(f"\033[32m   Github: {self.additional_text}\033[0m")  # Print in green color
        self.print_banner()
        print(f"\033[32m   {self.creator_nam}\033[0m")  # Print in green color
        print(f"\033[32m   Creator: {self.creator_name}\033[0m")  # Print in green color
        print(f"\033[32m   Instagram: {self.creator_instagram}\033[0m")  # Print in green color
        print(f"\033[32m   Github: {self.additional_text}\033[0m")  # Print in green color

        while True:
            original_url, custom_domain, phishing_keywords = self.get_user_input()

            try:
                # Basic input validation can be added here
                masked_url = self.mask_url(original_url, custom_domain, phishing_keywords)
                print("\nMasked URL:", masked_url)
                
                # Include creator's Instagram link
                creator_url = self.creator_instagram
                creator_masked_url = self.mask_url(creator_url, custom_domain, self.creator_name)
                print("   Creator's Masked Instagram URL:", creator_masked_url)
                
            except Exception as e:
                print(f"An error occurred: {e}")

            another_masking = input("\nDo you want to mask another URL? (yes/no): ").lower()
            if another_masking != 'yes':
                print("\nThank you for using the URL Masking Tool!")
                break

if __name__ == "__main__":
    creator_name = "374.karware"
    creator_nam = "Contact Info"
    creator_instagram = "Instagram - 374.karware_"
    additional_text = "https://github.com/termuse/masked_url"
    masking_tool = URLMaskingTool(creator_name, creator_instagram, additional_text)
    masking_tool.run()