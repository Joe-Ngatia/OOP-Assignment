abstract class BankAccount {
    protected String accountNumber;
    protected double balance;
    protected String ownerName;

    // Constructor
    public BankAccount(String accountNumber, String ownerName, double balance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        this.balance = balance;
    }

    // Abstract methods
    public abstract void deposit(double amount);
    public abstract void withdraw(double amount);

    // Concrete methods
    public double getBalance() {
        return balance;
    }

    public void displayInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Owner Name: " + ownerName);
        System.out.println("Balance: " + balance);
    }
}

class SavingsAccount extends BankAccount {

    public SavingsAccount(String accountNumber, String ownerName, double balance) {
        super(accountNumber, ownerName, balance);
    }

    @Override
    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited " + amount + " into Savings Account");
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn " + amount + " from Savings Account");
        } else {
            System.out.println("Insufficient funds in Savings Account");
        }
    }
}

class CurrentAccount extends BankAccount {

    public CurrentAccount(String accountNumber, String ownerName, double balance) {
        super(accountNumber, ownerName, balance);
    }

    @Override
    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited " + amount + " into Current Account");
    }

    @Override
    public void withdraw(double amount) {
        balance -= amount; // Allows overdraft
        System.out.println("Withdrawn " + amount + " from Current Account");
    }
}
//Interface
interface Transaction {
    void execute();
    String getDetails();
    double getAmount();
}
//Implementations of interfaces
class DepositTransaction implements Transaction {
    private BankAccount account;
    private double amount;

    public DepositTransaction(BankAccount account, double amount) {
        this.account = account;
        this.amount = amount;
    }

    @Override
    public void execute() {
        account.deposit(amount);
    }

    @Override
    public String getDetails() {
        return "Deposit of " + amount;
    }

    @Override
    public double getAmount() {
        return amount;
    }
}

class WithdrawalTransaction implements Transaction {
    private BankAccount account;
    private double amount;

    public WithdrawalTransaction(BankAccount account, double amount) {
        this.account = account;
        this.amount = amount;
    }

    @Override
    public void execute() {
        account.withdraw(amount);
    }

    @Override
    public String getDetails() {
        return "Withdrawal of " + amount;
    }

    @Override
    public double getAmount() {
        return amount;
    }
}

class TransferTransaction implements Transaction {
    private BankAccount fromAccount;
    private BankAccount toAccount;
    private double amount;

    public TransferTransaction(BankAccount fromAccount, BankAccount toAccount, double amount) {
        this.fromAccount = fromAccount;
        this.toAccount = toAccount;
        this.amount = amount;
    }

    @Override
    public void execute() {
        fromAccount.withdraw(amount);
        toAccount.deposit(amount);
    }

    @Override
    public String getDetails() {
        return "Transfer of " + amount + " from " + fromAccount.accountNumber +
               " to " + toAccount.accountNumber;
    }

    @Override
    public double getAmount() {
        return amount;
    }
}


public class BankingSystem {
    public static void main(String[] args) {

        // Create accounts
        BankAccount acc1 = new SavingsAccount("001", "Joseph", 1000);
        BankAccount acc2 = new CurrentAccount("002", "Mary", 500);

        // Display info
        acc1.displayInfo();
        acc2.displayInfo();

        System.out.println("\n--- Transactions ---");

        // Polymorphism using interface
        Transaction t1 = new DepositTransaction(acc1, 200);
        Transaction t2 = new WithdrawalTransaction(acc2, 100);
        Transaction t3 = new TransferTransaction(acc1, acc2, 300);

        Transaction[] transactions = {t1, t2, t3};

        for (Transaction t : transactions) {
            System.out.println(t.getDetails());
            t.execute();
            System.out.println();
        }

        // Final balances
        System.out.println("--- Final Balances ---");
        acc1.displayInfo();
        acc2.displayInfo();
    }
}