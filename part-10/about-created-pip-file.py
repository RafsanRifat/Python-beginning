# pipfile ===>>

    #pipfile a 4 ta section thake-->
        # 1) source --> eikhane packages gula jeikhan theke newa hoiche, seikhaner tottho thake
        # 2) dev packages
        # 3) packages --> jei packages gulo install kora hoiche virtual invironment a. r * er meaning holo- latest version
        # 4) requires --> the virsion of python

#pipfile.lock ===>> eita ekta Json file

    # This is a list of the dependencies of our application/projects with their version .


# project/application ta jodi onno kono computer a niyea jawa hoy, tahole sei computer er dependency/packages er version
# gulo jodi alada thake, tahole oneksomoy application/project oi alada computer a kaj nao korte pare.
# sei khetre pip file r pipfile.lock kaj a asbe. pip file r pipfile.lock a sob dependency er details thake. seikhan theke
# command er maddhome notun computer a proyojonio packages/dependency gulo install kore nilei hobe.


# notun computer a jeye--->> (pipenv install)  ei command chalaile abar dependency gulo install hobe virtual environment
# a... kintu eikhane version er somossa hoite pare. notun computer er version onujayee package gulo install hoite pare.

# jodi development er exact version install korte chawa hoy, tahole, pipfile ignore kore pipfile.lock k follow kore
# dependency ba packages gulo install korte hobe ====>>>

        # pipenv install --ignore-pipfile