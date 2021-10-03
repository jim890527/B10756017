using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace the_day_of_the_week
{
    public class Global
    {
        public static int c, y, m, d;//練習宣告全域變數
    }
    class Program
    {        
        static void Main(string[] args)
        {
            int choice;
            do
            {
                Console.WriteLine("the_day_of_the_week");
                Console.WriteLine("1.quit 2.input data");
                choice = int.Parse(Console.ReadLine());
                if (choice == 1 || choice == 2)//選擇錯誤跳出錯誤訊息
                {
                    switch (choice)
                    {
                        case 1:
                            break;
                        case 2:
                            Console.WriteLine("input data(including year, month, and day. ex.20000527)");//請照ex格式輸入
                            string in1 = Console.ReadLine();
                            if (in1.Length == 8)//判斷格式是否正確
                            {
                                Global.c = int.Parse(in1.Substring(0, 2));//讀取子字串用
                                Global.m = int.Parse(in1.Substring(4, 2)) - 2;//讀取子字串用
                                Global.d = int.Parse(in1.Substring(6, 2));//讀取子字串用
                                if (Global.m == -1 || Global.m == 1 || Global.m == 3 || Global.m == 5 || Global.m == 6 || Global.m == 8 || Global.m == 10)
                                {
                                    if (Global.d <= 31 && Global.d >= 1)
                                    {
                                        Dofw(in1);//副程式
                                    }
                                    else
                                        Console.WriteLine("ERROR1\r\n");//ERROR1代表日期錯誤
                                }
                                else if (Global.m == 2 || Global.m == 4 || Global.m == 7 || Global.m == 9)
                                {
                                    if (Global.d <= 30 && Global.d >= 1)
                                    {
                                        Dofw(in1);//副程式
                                    }
                                    else
                                        Console.WriteLine("ERROR1\r\n");//ERROR1代表日期錯誤
                                }
                                else if (Global.m == 0 && Global.d <= 29)
                                {
                                    if (Global.d <= 29 && Global.d >= 1)
                                    {
                                        Dofw(in1);//副程式
                                    }
                                    else
                                        Console.WriteLine("ERROR1\r\n");//ERROR1代表日期錯誤
                                }
                                else
                                    Console.WriteLine("ERROR2\r\n");//ERROR2代表月份錯誤
                            }
                            else
                                Console.WriteLine("ERROR3\r\n");//ERROR3代表輸入格式錯誤
                            break;
                    }
                }
                else
                    Console.WriteLine("ERROR4\r\n");//ERROR4代表選項選擇錯誤
            } while (choice != 1);//除非選擇quit否則Program不會停止
        }
        static void Dofw(string in1)//減少相同的程式碼
        {
            double week;
            if (Global.m == 0 || Global.m == -1)//參照公式
            {
                Global.y = int.Parse(in1.Substring(2, 2)) - 1;
                if (Global.y < 0)
                    Global.y = 99;
                if (Global.m == 0)
                    Global.m = 12;
                else
                    Global.m = 11;
            }
            else
                Global.y = int.Parse(in1.Substring(2, 2));
            week = Math.Floor((Global.d + (2.6 * Global.m - 0.2) + 5 * (Global.y % 4) + 3 * Global.y + 5 * (Global.c % 4)) % 7);//math.floor為無條件捨去小數點
            switch (week)
            {
                case 1:
                    Console.WriteLine("Monday\r\n");
                    break;
                case 2:
                    Console.WriteLine("Tuesday\r\n");
                    break;
                case 3:
                    Console.WriteLine("Wednesday\r\n");
                    break;
                case 4:
                    Console.WriteLine("Thursday\r\n");
                    break;
                case 5:
                    Console.WriteLine("Friday\r\n");
                    break;
                case 6:
                    Console.WriteLine("Saturday\r\n");
                    break;
                case 0:
                    Console.WriteLine("Sunday\r\n");
                    break;
            }
        }
    }
}
