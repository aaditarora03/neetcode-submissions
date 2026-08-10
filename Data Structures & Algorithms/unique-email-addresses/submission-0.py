class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            clean_local = local.split('+')[0]
            clean_local = clean_local.replace('.','')
            unique_emails.add(clean_local + "@" + domain)
        return len(unique_emails)