using System;

namespace Convert_currency
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1,num2;
            Console.WriteLine("輸入金額(整數):");
            int ntd = int.Parse(Console.ReadLine());
            do {   
                Console.WriteLine("輸入欲交換外幣號碼1:\r\n 1.USD  2.SEK  3.HKD  4.NZD  5.GBP  6.THB  \r\n 7.AUD  8.PHP  9.CAD 10.IDR 11.SGD 12.EUR \r\n13.CHF 14.KRW 15.JPY 16.VND 17.CNY 18.MYR");
                num1 = int.Parse(Console.ReadLine());
                Console.WriteLine("輸入欲交換外幣號碼2:\r\n 1.USD  2.SEK  3.HKD  4.NZD  5.GBP  6.THB  \r\n 7.AUD  8.PHP  9.CAD 10.IDR 11.SGD 12.EUR \r\n13.CHF 14.KRW 15.JPY 16.VND 17.CNY 18.MYR");
                num2 = int.Parse(Console.ReadLine());
                double ans1=0,ans2=0;
                string str1="", str2="";
                if (num1 >= 1 && num1 <= 18 && num2 >= 1 && num2 <= 18)
                {
                    switch (num1)
                    {
                        case 1:
                            ans1 = ntd * 32.82;
                            str1 = "USD";
                            break;
                        case 2:
                            ans1 = ntd * 3.49;
                            str1 = "SEK";
                            break;
                        case 3:
                            ans1 = ntd * 4.113;
                            str1 = "HKD";
                            break;
                        case 4:
                            ans1 = ntd * 21.6;
                            str1 = "NZD";
                            break;
                        case 5:
                            ans1 = ntd * 45.21;
                            str1 = "GBP";
                            break;
                        case 6:
                            ans1 = ntd * 0.8312;
                            str1 = "THB";
                            break;
                        case 7:
                            ans1 = ntd * 23.3;
                            str1 = "AUD";
                            break;
                        case 8:
                            ans1 = ntd * 0.6506;
                            str1 = "PHP";
                            break;
                        case 9:
                            ans1 = ntd * 24.14;
                            str1 = "CAD";
                            break;
                        case 10:
                            ans1 = ntd * 0.00218;
                            str1 = "IDR";
                            break;
                        case 11:
                            ans1 = ntd * 23.11;
                            str1 = "SGD";
                            break;
                        case 12:
                            ans1 = ntd * 35.44;
                            str1 = "EUR";
                            break;
                        case 13:
                            ans1 = ntd * 32.49;
                            str1 = "CHF";
                            break;
                        case 14:
                            ans1 = ntd * 0.02509;
                            str1 = "KRW";
                            break;
                        case 15:
                            ans1 = ntd * 0.2866;
                            str1 = "JPY";
                            break;
                        case 16:
                            ans1 = ntd * 0.00128;
                            str1 = "VND";
                            break;
                        case 17:
                            ans1 = ntd * 4.968;
                            str1 = "CNY";
                            break;
                        case 18:
                            ans1 = ntd * 6.74;
                            str1 = "MYR";
                            break;
                    }
                    switch(num2)
                    {
                        case 1:
                            ans2 = ans1 / 32.82;
                            str2 = "USD";
                            break;
                        case 2:
                            ans2 = ans1 / 3.49;
                            str2 = "SEK";
                            break;
                        case 3:
                            ans2 = ans1 / 4.113;
                            str2 = "HKD";
                            break;
                        case 4:
                            ans2 = ans1 / 21.6;
                            str2 = "NZD";
                            break;
                        case 5:
                            ans2 = ans1 / 45.21;
                            str2 = "GBP";
                            break;
                        case 6:
                            ans2 = ans1 / 0.8312;
                            str2 = "THB";
                            break;
                        case 7:
                            ans2 = ans1 / 23.3;
                            str2 = "AUD";
                            break;
                        case 8:
                            ans2 = ans1 / 0.6506;
                            str2 = "PHP";
                            break;
                        case 9:
                            ans2 = ans1 / 24.14;
                            str2 = "CAD";
                            break;
                        case 10:
                            ans2 = ans1 / 0.00218;
                            str2 = "IDR";
                            break;
                        case 11:
                            ans2 = ans1 / 23.11;
                            str2 = "SGD";
                            break;
                        case 12:
                            ans2 = ans1 / 35.44;
                            str2 = "EUR";
                            break;
                        case 13:
                            ans2 = ans1 / 32.49;
                            str2 = "CHF";
                            break;
                        case 14:
                            ans2 = ans1 / 0.02509;
                            str2 = "KRW";
                            break;
                        case 15:
                            ans2 = ans1 / 0.2866;
                            str2 = "JPY";
                            break;
                        case 16:
                            ans2 = ans1 / 0.00128;
                            str2 = "VND";
                            break;
                        case 17:
                            ans2 = ans1 / 4.968;
                            str2 = "CNY";
                            break;
                        case 18:
                            ans2 = ans1 / 6.74;
                            str2 = "MYR";
                            break;
                    }
                    Console.WriteLine(ntd + str1 + " = " + ans2 + str2 );
                }
                else
                    Console.WriteLine("號碼輸入錯誤請重新輸入\r\n");
            }while (num1 < 1 || num1 > 18 || num2 < 1 || num2 > 18);
            Console.ReadLine();
        }
    }
}
