class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if start > end:
            return 0

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def day_of_year(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(days[:month - 1]) + day

        return day_of_year(end) - day_of_year(start) + 1
