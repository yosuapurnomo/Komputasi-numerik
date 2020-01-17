
public class Main {
    
    static int M = 10; 
  
    // Fungsi untuk print matrix nya
    static void PrintMatriks(float a[][], int n) 
    { 
        for (int i = 0; i < n; i++)  
        { 
            for (int j = 0; j <= n; j++)  
            System.out.printf("%.3f ", a[i][j]); 
            System.out.println(); 
        } 
    }
    
    // fungsi untuk mengurangi
    // baris eselon
    static int Hitung(float a[][], int n) 
    { 
        int i, j, k = 0, c, flag = 0, m = 0; 
        float pro = 0; 
      
        // Performing elementary operations 
        for (i = 0; i < n; i++) 
        {
            if (a[i][i] == 0)  
            {
                c = 1; 
                while (a[i + c][i] == 0 && (i + c) < n)  
                    c++;          
                    if ((i + c) == n)  
                    { 
                        flag = 1; 
                        break; 
                    }
                    for (j = i, k = 0; k <= n; k++)  
                    { 
                        float temp =a[j][k]; 
                        a[j][k] = a[j+c][k]; 
                        a[j+c][k] = temp; 
                    } 
                }
  
                for (j = 0; j < n; j++)  
                {
              
                    // Kecuali i == j 
                    if (i != j)  
                    {
                        
                        // menjadikan matrix ke eselon baris yang
                        // sudah dikurangi
                        float p = a[j][i] / a[i][i]; 
                        
                    for (k = 0; k <= n; k++)                  
                        a[j][k] = a[j][k] - (a[i][k]) * p;            
                    } 
                } 
        }
    return flag; 
    }
    
    // fungsi untuk menampilkan hasil yang di inginkan 
    // jika ada solusi yang unik
    // tidak menampilkan solusi atau terus  
    // tergantung input yang diberikan
    static void PrintHasil(float a[][], int n, int flag) 
    {
        System.out.println("Hasil X nya adalah : "); 

        if (flag == 2)    
        System.out.println("Ada solusi tak terhingga");  
        else if (flag == 3)   
        System.out.println("Tidak ada solusi!"); 
      
        // print dengan membagi konstanta dari masing
        // masing element diagonal 
        else { 
                for (int i = 0; i < n; i++){
                    System.out.print("X" + (i+1) + " : ");
                    System.out.printf("%.3f ", a[i][n] / a[i][i]);
                }
                System.out.println("");
            } 
    }
    
    // To check whether infinite solutions  
    // exists or no solution exists 
    static int CekKonsisten(float a[][], int n, int flag) 
    {
        int i, j; 
        float sum; 

        // flag == 2 for infinite solution 
        // flag == 3 for No solution 
        flag = 3; 
        for (i = 0; i < n; i++)  
        { 
            sum = 0; 
            for (j = 0; j < n; j++)   
                sum = sum + a[i][j]; 
                if (sum == a[i][j])  
                flag = 2;     
        } 
    return flag; 
    }

    public static void main(String[] args) {
        // TODO code application logic here
        float a[][] = {{ 2, -1, 3, -1, 11 },  
                    { -1, -2, -1, -1, -4 },  
                    { 3, 3, -1, -3, -2 },
                    { -2, 2, -2, 2, 4 }}; 
                      
        // Order of Matrix(n) 
        int n = 4, flag = 0; 

        // Performing Matrix transformation 
        flag = Hitung(a, n); 
      
        if (flag == 1)    
            flag = CekKonsisten(a, n, flag);  
  
        // Printing Final Matrix 
        System.out.println("Hasil akhir matrix nya adalah : "); 
        PrintMatriks(a, n); 
        System.out.println(""); 
      
        // Printing Solutions(if exist) 
        PrintHasil(a, n, flag);
    }
}
