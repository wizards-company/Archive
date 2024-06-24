import "./globals.css";
import Header from "@/components/Header";

export const metadata = {
  title: "Libs",
  description: "Ganhe livros através de doações",
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body>
        <Header />
        {children}
      </body>
    </html>
  );
}
