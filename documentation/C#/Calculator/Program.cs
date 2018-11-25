using System;
using System.Text;
using System.Windows.Form;
using System.Threading.Tasks;

namespace Calculator
{
    public partial class Program : Form
    {
        public Calculator()
        {
            InitializeComponent();
        }
        private void HelloLabel_Click(object sender, EventArgs e)
        {
            int number1 = 1;
            int number2 = 2;

            int sum = number1 + number2;
            HelloLabel.Text = sum.ToString(); // HelloLabel.Text : string

            
        }
    }
}
