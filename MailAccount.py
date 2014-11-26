import imaplib

class MailAccount():
    '''
        This hold email account
        type email properties is in dictionary
        account = {'amru@gmail.com':{'username':'amru@gmail.com',
                                    'password':'password',
                                    'host':'mail.google.com',
                                    'use_ssl':True/False, #optional
                                    'port':IMAP4_PORT, #optional
                                    'keyfile':None, #optional only for use_ssl
                                    'certfile':None, #optional only for use_ssl
                                    }}
    '''
    def __init__(self, account={}):
        
        # init account using IMAP4 connection
        self.__mail_connection = {}
        
        # mail account
        self.__account = {}
        
        if len(account):
            self.add_account(account)
        
    # add account into MailAccountlist
    # account should be in dictionary format
    def add_account(self, account):
        for account_name in account:
            # check if account already in _account?
            if not self.__account.get(account_name):
            
                self.__account[account_name] = account[account_name]
                
                self.__init_imap4(account_name)
                
    # init imap account
    # this will init imap4 instance
    def __init_imap4(self, account_name):
        # check imap4 instance
        if self.__mail_connection.get(account_name):
            self.__mail_connection[account_name].close()
            self.__mail_connection[account_name].logout()
                    
        # init imap4 instance
        # check if use ssl or not
        account_info = self.__account.get(account_name)
        
        if account_info:
            if account_info.get('use_ssl'):
                # default port
                port = imaplib.IMAP4_SSL_PORT
                keyfile = None
                certfile = None
                if account_info.get('port'):
                    port = account_info.get('port')
                
                if account_info.get('keyfile'):
                    keyfile = account_info.get('keyfile')
                    
                if account_info.get('certfile'):
                    certfile = account_info.get('certfile')
                    
                self.__mail_connection[account_name] = imaplib.IMAP4_SSL(account_info.get('host'), port, keyfile, certfile)
            else:
                # default port
                port = imaplib.IMAP4_PORT
                if account_info.get('port'):
                    port = account_info.get('port')
                    
                self.__mail_connection[account_name] = imaplib.IMAP4(account_info.get('host'), port)
                
    def logout_account(self, account_name):
        print()
    # close logout imap4
    def logout_account(self, account_name):
        if self.__mail_connection.get(account_name):
            self.__mail_connection[account_name].close()
            self.__mail_connection[account_name].logout()
			
	# login account
    def login_account(self, account_name):
		# check if connection exist
        mail_connection = self.__mail_connection.get(account_name)
        if mail_connection:
            # check if account info exist
            account_info = self.__account.get(account_name)
            if account_info:
                mail_connection.login(account_info.get('username'), account_info.get('password'))
			
        
    # remove account from mail account
    # account_name is dictionary key
    def remove_account(self, account_name):
        if self.__mail_connection.get(account_name):
            self.logout_account(account_name)
            self.__mail_connection.pop(account_name)
            
            self.__account.pop(account_name)
        
    # update account information
    # account should be in dictionary format
    def update_account(self, account):
        for account_name in account:
            if self.__account.get(account_name):
            
                # extract updated value
                for account_name_setup in account[account_name]:
                
                    self.__account[account_name][account_name_setup] = account[account_name][account_name_setup]
                    
                self.__init_imap4(account_name)
                    
    # get account
    def get_account(self, account_key=()):
    
        account_info = {}
        
        if len(account_key):
            # get account information from _account
            # store to account_info then return
            for account_item in account_key:
                account_info[account_item] = self.__account.get(account_item)
                
            return account_info
            
        else:
            return self.__account
                    
            
