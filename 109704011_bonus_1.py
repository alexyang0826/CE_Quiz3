import hashlib

HASH1 = '5f4dcc3b5aa765d61d8327deb882cf99'
HASH2 = '5a105e8b9d40e1329780d62ea2265d8a'
common_passwords = [
    "123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123",
    "abc123", "qwertyuiop", "admin", "welcome", "monkey", "login", "abc123456", "654321", "passw0rd", "letmein",
    "football", "1234567890", "superman", "michael", "sunshine", "master", "666666", "1234", "11111111", "batman",
    "starwars", "123456a", "dragon", "liverpool", "iloveu", "000000", "princess", "qwerty123", "654321", "lovely",
    "qwertyui", "7777777", "baseball", "iloveyou1", "123qwe", "jennifer", "asdfgh", "hunter", "password1", "welcome1",
    "jordan23", "charlie", "solo", "jessica", "ginger", "james", "secret", "daniel", "cynthia", "babygirl", "hannah",
    "love", "whatever", "987654321", "tigger", "football1", "fuckyou", "cheese", "internet", "alex", "morgan", "andrew",
    "badboy", "jordan", "pakistan", "purple", "batman1", "trustno1", "samantha", "123456789a", "hello", "michelle",
    "matthew", "killer", "nicole", "justin", "amanda", "snoopy", "dolphin", "mustang", "pepper", "melissa", "123abc",
    "myspace1", "pokemon", "super", "chocolate", "chelsea", "696969", "biteme", "marilyn", "albert", "bigdog",
    "jackson", "test1", "robert", "lovers", "amanda1", "joseph", "killer1", "happy", "hello1", "babyboy", "charlotte",
    "mickey",
    "rosebud", "guitar", "buster", "george", "marryme", "herman", "morgan1", "charlie1", "qwerty12", "steven", "peter",
    "silver", "marcus", "william", "peterpan", "freedom", "marina", "tomcat", "dallas", "scooby", "walter", "thomas",
    "harrypotter", "maddog", "georgia", "cassie", "katie", "thunder", "winner", "hello123", "test123", "looking",
    "nintendo", "amanda123", "abcdef", "heather", "benjamin", "131313", "sarah", "asdfghjkl", "scoobydoo", "hardcore",
    "qwertyuiop123", "1q2w3e4r", "apollo", "internet1", "orange", "jamesbond",
    "12345678910", "12345678901", "12345678902", "12345678903", "12345678904", "12345678905", "12345678906", "pa55w0rd",
    "football2", "firebird", "zaq12wsx", "sunflower", "sexygirl", "peaches", "qwerty1234", "banana", "flower",
    "shadow", "monkey1", "jesus", "hello1234", "samsung", "iloveyou123", "samantha1", "london", "justin1", "mustang1",
    "johnny", "maggie", "yamaha", "soccer", "qazwsx", "chicken", "121212", "madison", "computer", "1234qwer", "jesus1",
    "julian", "fender", "brandon", "football12", "monkey12", "a123456", "mariah", "qwer1234", "trust", "monkey123",
    "george1", "q1w2e3r4t5", "abcdefg", "banana1", "freddie", "diamond", "jordan1", "mustanggt", "hannah1", "bigdaddy",
    "trouble", "ranger", "stupid", "babydoll", "crystal", "sebastian", "karina", "johnson", "ashley1", "sunshine1",
    "jackson1", "qwer123", "butterfly", "love123", "daniel1", "lindsey", "purple1", "pretty", "myspace", "jessica1",
    "charlie123", "qazwsxedc", "maria", "mexico", "taylor1", "stephen", "summer", "tigger1", "james1", "butterfly1",
    "shadows", "brandon1", "buddy", "matthew1", "mickey1", "soccer1", "peanut", "sammy", "anthony", "diamond1",
    "whatever1", "brandy", "andrea", "iceman", "john316", "september", "jennifer1", "rabbit", "tiffany", "yamaha1",
    "cinderella", "emily1", "superman1", "joshua1", "iloveyou2", "blondie", "jesus123", "hotmail", "carolina",
    "williams", "madison1", "nicole1", "melissa1", "roses", "richard", "sabrina", "ferrari", "barney", "loveyou",
    "baby123", "london1", "haley", "scooter", "thomas1", "cheerleader", "knight", "nicholas", "mariah1", "candice",
    "aaaaaa", "mercedes", "april", "jimmy", "pookie", "jordan123", "player", "chelsea1", "joseph1", "kelly", "david1",
    "gandalf", "tiffany1", "jason1", "valentina", "friend", "joseph123", "monster", "faith", "joshua123", "angelina",
    "princess1", "rebecca1", "iloveyou!", "babyblue", "orange1", "jacob1", "abcdef123", "superman123", "lovely1",
    "bigboobs", "computer1", "qweasdzxc", "iloveyou", "michael1", "michael123", "michael", "michael123", "michael1"]


def hack_password(password):
    print(f'[*] Cracking password: {password}...')
    for word in common_passwords:
        guess = hashlib.md5(word.encode('utf-8')).hexdigest()
        if guess.upper() == password or guess.lower() == password:
            print(f'[+] Password found: {word}')
            print('[+] Exiting...')
            print('_______________________________________________________')
            return
        else:
            print(f'[-] Guess: {word} incorrect... {guess}')
    print(f'Password not found in wordlist...')


if __name__ == '__main__':
    hack_password(HASH1)
    hack_password(HASH2)
