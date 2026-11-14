def getRow(self, rowIndex: int) -> list[int]:
        row=[1]
        current=1
        for i in range(1,rowIndex+1):
            next_val=current*(rowIndex-i+1)//i
            row.append(next_val)
            current=next_val
        return row
        