from instapy import InstaPy
import getpass

print('''

██╗███╗░░██╗░██████╗████████╗░█████╗░██████╗░░█████╗░████████╗
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██████╦╝██║░░██║░░░██║░░░
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══██╗██║░░██║░░░██║░░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██████╦╝╚█████╔╝░░░██║░░░
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░
𝕓𝕪 𝔸𝕜𝕤𝕙𝕒𝕪 ℝ𝔽

''')
no_com = False
insta_username = input("username: ").strip()
insta_password = getpass.getpass()
comm = input("set comments (seperate with space | leave empty to disable commenting): ").strip()
tag = input("set tags (seperate with space): ").strip()
com_list = []
tag_list = []

if len(comm) < 1:
	no_com = True

else:
	com_list = comm.split()

tag_list = tag.split()

try:
	session = InstaPy(username=insta_username, password=insta_password)
	session.login()


	session.set_relationship_bounds(enabled=True,
					potency_ratio=-1.21,
					delimit_by_numbers=True,
					max_followers=4590,
						max_following=5555,
						min_followers=45,
						min_following=77)
	if no_com:
		session.set_do_comment(True, percentage=10)
		session.set_comments(com_list)

	session.set_dont_include(['friend1', 'friend2', 'friend3'])
	session.like_by_tags(tag_list, amount=100)


	session.end()

except Exception as error:
    print('ERROR', error)                                                            