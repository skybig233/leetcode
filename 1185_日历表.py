class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def daysOfDate(day: int, month: int, year: int)->int:
            """
            将输入日期映射到某一正整数上，即：
            1年1月1号映射为1
            2年1月1号映射为366
            :param day: 取值范围1-31
            :param month: 取值范围1-12
            :param year:正整数
            :return:
            """
            feb_days=29 if isLeapYear(year) else 28
            month_days=[31,feb_days,31,30,31,30,31,31,30,31,30,31]

            add1=day# 1月1号映射为1
            add2=sum(month_days[:month - 1])# 8月1号与1月1号之间相差的天数，就是把1-7月对应的天数相加
            add3=sum(366 if isLeapYear(i) else 365 for i in range(1,year))

            sum_days=add1+add2+add3
            return sum_days

        def isLeapYear(year:int)->bool:
            """
            判断闰年
            四年一润，百年不润，四百年又润
            """
            if year%4==0 and year%100!=0 or year%400==0:
                return True
            else:
                return False

        f_date=daysOfDate(day,month,year)
        print(f_date)
        enum_week=("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        return enum_week[f_date % 7]

s=Solution().dayOfTheWeek(day = 3, month = 1, year = 2022)
print(s)