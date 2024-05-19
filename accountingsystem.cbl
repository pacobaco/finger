IDENTIFICATION DIVISION.
PROGRAM-ID. AccountingSystem.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT TransFile ASSIGN TO "transactions.dat"
        ORGANIZATION IS LINE SEQUENTIAL.
    SELECT LedgerFile ASSIGN TO "ledger.dat"
        ORGANIZATION IS LINE SEQUENTIAL.

DATA DIVISION.
FILE SECTION.
FD  TransFile.
01  TransRecord.
    05  TransType       PIC X(10).
    05  TransAmount     PIC 9(9)V99.
    05  TransAccount    PIC X(10).

FD  LedgerFile.
01  LedgerRecord.
    05  AccountName     PIC X(10).
    05  AccountBalance  PIC 9(9)V99.

WORKING-STORAGE SECTION.
01  WS-EOF              PIC X VALUE "N".
01  WS-TransAmount      PIC 9(9)V99.
01  WS-TransAccount     PIC X(10).
01  WS-AccountFound     PIC X VALUE "N".

77  TOTAL-DEBITS       PIC 9(9)V99 VALUE 0.
77  TOTAL-CREDITS      PIC 9(9)V99 VALUE 0.
77  LINE               PIC X(80).

PROCEDURE DIVISION.
MAIN-LOGIC.
    PERFORM INITIATE-FILES
    PERFORM PROCESS-TRANSACTIONS
    PERFORM CLOSE-FILES
    STOP RUN.

INITIATE-FILES.
    OPEN INPUT TransFile
    OPEN I-O LedgerFile.

PROCESS-TRANSACTIONS.
    READ TransFile INTO TransRecord
        AT END SET WS-EOF TO "Y".
    PERFORM UNTIL WS-EOF = "Y"
        MOVE TransAmount TO WS-TransAmount
        MOVE TransAccount TO WS-TransAccount
        PERFORM UPDATE-LEDGER
        READ TransFile INTO TransRecord
            AT END SET WS-EOF TO "Y"
    END-PERFORM.

UPDATE-LEDGER.
    MOVE "N" TO WS-AccountFound
    READ LedgerFile INTO LedgerRecord
        AT END DISPLAY "Account not found."
    PERFORM UNTIL WS-AccountFound = "Y"
        IF AccountName = WS-TransAccount
            ADD WS-TransAmount TO AccountBalance
            MOVE "Y" TO WS-AccountFound
            REWRITE LedgerRecord
        ELSE
            DISPLAY "Account not found."
        END-IF
        READ LedgerFile INTO LedgerRecord
            AT END MOVE "Y" TO WS-AccountFound
    END-PERFORM.

CLOSE-FILES.
    CLOSE TransFile
    CLOSE LedgerFile.

END PROGRAM AccountingSystem.
