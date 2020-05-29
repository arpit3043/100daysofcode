def email_list(domains):
	emails = []
	for dom,users in domains.items():
		for user in users:
			emails.append(user+"@"+dom)
			return(emails)