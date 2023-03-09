using System;
using System.Drawing;
using System.Windows.Forms;

namespace HolaMundo
{
    public class HolaMundoForm : Form
    {
        public HolaMundoForm()
        {
            Text = "Hola mundo";
            ClientSize = new Size(300, 100);

            var label = new Label
            {
                Text = "Hola mundo",
                Font = new Font(FontFamily.GenericSansSerif, 20, FontStyle.Bold),
                Location = new Point(50, 30),
                Size = new Size(200, 50)
            };
            Controls.Add(label);
        }

        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new HolaMundoForm());
        }
    }
}
