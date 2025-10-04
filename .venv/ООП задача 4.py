class PasswordChecker:
    def set_password_range(self,min_len,max_len):
        self.min_len = min_len
        self.max_len = max_len
    def check_passwords(self, passwords):
        results = []

        for password in passwords:
            if self.min_len <= len(password)<= self.max_len:
                results.append(True)
            else:
                results.append(False)
        return results
checker1 = PasswordChecker()
checker1.set_password_range(5, 10)
print(checker1.min_len, checker1.max_len)
print(checker1.check_passwords(['qwer', 'fool67', 'ghjo478hl404']))

