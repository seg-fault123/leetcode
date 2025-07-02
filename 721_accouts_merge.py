class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_index = defaultdict(list) # email is the key, which accounts/indices it belongs to is the list associated to it
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email_index[account[j]].append(i)
        
        visited = [False]*len(accounts)

        def dfs(index, emails):
            visited[index] = True

            # for each email in the current account index, get all other accounts which also contain the email and populate the 'emails' set
            account = accounts[index]
            for j in range(1, len(account)):
                email = account[j]
                emails.add(email) # all emails of the current account will be merged. Moreover all accounts which contain this email will also be visited and their emails will also be added recursively.
                for neighbor in email_index[email]:
                    if not visited[neighbor]:
                        dfs(neighbor, emails)
            
            return
        
        result = []
        for i in range(len(accounts)):
            if visited[i]:
                continue
            
            name = accounts[i][0]
            emails = set()
            dfs(i, emails)
            result.append([name]+sorted(emails))
        
        return result
            


