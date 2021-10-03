using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simple_calculator_diffcult
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> num = new List<string>();
            List<string> ope = new List<string>();
            string in1;
            Console.WriteLine("input number(integer or floating-point):");
            in1 = Console.ReadLine();
            num.Add(in1);//將in1丟入num中
            while (in1 != "quit")//輸入quit結束
            {
                string Operator1;
                float ans;
                Console.WriteLine("input what operation will be performed(+ - * / =):");
                Operator1 = Console.ReadLine();
                if (Operator1 == "+" || Operator1 == "-")
                {
                    if (ope.Count > 0)
                    {
                        if (ope[ope.Count - 1] == "*" || ope[ope.Count - 1] == "/")//若輸入+或-則判斷前面有無*或/
                        {
                            for (int i = ope.Count-1; i >= 0; i--)//若有則將ope[]stack出來進入num[]
                            {
                                num.Add(ope[i]);
                                ope.RemoveAt(i);//刪除ope裡的運算子
                            }
                            ope.Add(Operator1);//執行完畢將+或-丟入ope(此時ope剩下一個運算子)
                        }
                        else
                            ope.Add(Operator1);
                    }
                    else
                        ope.Add(Operator1);
                }
                else if (Operator1 == "*" || Operator1 == "/")//*或/直接丟進ope
                    ope.Add(Operator1);
                if (Operator1 == "=")
                {
                    for (int i = ope.Count-1; i >= 0; i--)//將剩餘的ope丟進num做運算
                    {
                        num.Add(ope[i]);
                        ope.RemoveAt(i);//清除ope
                    }
                    for(int i=0;i<num.Count; i++)
                    {
                        if(num[i] == "+" || num[i] == "-" || num[i] == "*" || num[i] == "/")//讀取到num裡的運算子時執行運算
                        {
                            switch (num[i])
                            {
                                case "+":
                                    ans = float.Parse(num[i - 2]) + float.Parse(num[i - 1]);//清除num[i]及num[i-1]將運算結果丟進num[i-2]，其餘會自動往前遞補
                                    num[i - 2] = Convert.ToString(ans);
                                    num.RemoveAt(i);
                                    num.RemoveAt(i-1);
                                    //Console.WriteLine(num[i-2]);
                                    i = 0 ;
                                    break;
                                case "-":
                                    ans = float.Parse(num[i - 2]) - float.Parse(num[i - 1]);//清除num[i]及num[i-1]將運算結果丟進num[i-2]，其餘會自動往前遞補
                                    num[i - 2] = Convert.ToString(ans);
                                    num.RemoveAt(i);
                                    num.RemoveAt(i - 1);
                                    //Console.WriteLine(num[i - 2]);
                                    i = 0;
                                    break;
                                case "*":
                                    ans = float.Parse(num[i - 2]) * float.Parse(num[i - 1]);//清除num[i]及num[i-1]將運算結果丟進num[i-2]，其餘會自動往前遞補
                                    num[i - 2] = Convert.ToString(ans);
                                    num.RemoveAt(i);
                                    num.RemoveAt(i - 1);
                                    //Console.WriteLine(num[i - 2]);
                                    i = 0;
                                    break;
                                case "/":
                                    ans = float.Parse(num[i - 2]) / float.Parse(num[i - 1]);//清除num[i]及num[i-1]將運算結果丟進num[i-2]，其餘會自動往前遞補
                                    num[i - 2] = Convert.ToString(ans);
                                    num.RemoveAt(i);
                                    num.RemoveAt(i - 1);
                                    //Console.WriteLine(num[i - 2]);
                                    i = 0;
                                    break;
                            }
                        }
                    }
                    Console.WriteLine("ANS:" + num[0]);//最後答案會在num[0]
                    num.RemoveAt(0);//清除答案，重新計算
                }
                Console.WriteLine("input number(integer or floating-point):");
                in1 = Console.ReadLine();
                num.Add(in1);
            }
        }
    }
}

