from MailAccount import MailAccount

account = {'amru.rosyada@gmail.com':{'username':'amru.rosyada@gmail.com',
                                        'host':'imap.gmail.com',
                                        'password':'tigerbrave86google',
                                        'use_ssl':True}}
                                        
mail_account = MailAccount(account)
print(mail_account.get_account())
mail_account.login_account('amru.rosyada@gmail.com')
