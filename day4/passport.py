
class Passport():
    byr = None #Birth Year
    iyr = None #Issue Year
    eyr = None #Expeiration Year
    hgt = None #Height
    hcl = None #Hair Color
    ecl = None #Eye Color
    pid = None #Passport ID
    cid = None #Country ID

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def isValidOne(self):
        if not self.byr or not self.iyr or not self.eyr or not self.hgt or not self.hcl or not self.ecl or not self.pid:
            return False
        return True


    def isValidTwo(self):
        return self.isValidByr() and self.isValidIyr() and self.isValidEyr() and self.isValidHgt() and self.isValidHcl() and self.isValidEcl() and self.isValidPid()

    def isValidByr(self):
        if self.byr and len(self.byr) == 4:
            year = int(self.byr)
            return year >= 1920 and year <= 2002
        return False
    
    def isValidIyr(self):
        if self.iyr and len(self.iyr) == 4:
            year = int(self.iyr)
            return year >= 2010 and year <= 2020
        return False

    def isValidEyr(self):
        if self.eyr and len(self.eyr) == 4:
            year = int(self.eyr)
            return year >= 2020 and year <= 2030
        return False

    def isValidHgt(self):
        if self.hgt and len(self.hgt) > 2:
            kind = self.hgt[-2:]
            if kind == 'cm':
                value = int(self.hgt[:-2])
                return value >= 150 and value <= 193
            elif kind == 'in':
                value = int(self.hgt[:-2])
                return value >= 59 and value <= 76
            return False
        return False

    def isValidHcl(self):
        if self.hcl and self.hcl[0] == "#" and len(self.hcl) == 7:
            validchars = set(['a', 'b', 'c', 'd', 'e', 'f'])
            for x in range(1, len(self.hcl)):
                if not self.hcl[x].isdigit() and not self.hcl[x] in validchars:
                    return False
            return True
        return False
    
    def isValidEcl(self):
        if self.ecl:
            validColors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
            return self.ecl in validColors
        return False

    def isValidPid(self):
        if self.pid:
            if len(self.pid) == 9:
                for x in self.pid:
                    if not x.isdigit():
                        return False
                return True
            return False
        return False
