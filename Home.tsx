import { useState, useRef } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { Copy, Download, Mail, CheckCircle2, Image as ImageIcon } from "lucide-react";
import { toast } from "sonner";
// import { LOGO_MMB_BASE64 } from "@/logo-base64";
import domtoimage from "dom-to-image";

export default function Home() {
  const [nome, setNome] = useState("Nome do Colaborador");
  const [departamento, setDepartamento] = useState("Departamento do Colaborador");
  const [email, setEmail] = useState("email@grupommb.com");
  const [copied, setCopied] = useState(false);
  const [downloading, setDownloading] = useState(false);
  const signatureRef = useRef<HTMLDivElement>(null);

  const htmlCode = `<table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, sans-serif; max-width: 650px;">
  <tr>
    <td style="padding-right: 20px; vertical-align: middle;">
      <div style="font-size: 22px; font-weight: bold; color: #00203f; margin-bottom: 8px;">${nome}</div>
      <div style="font-size: 16px; color: #444; margin-bottom: 12px;">${departamento}</div>
      <div style="height: 2px; background: linear-gradient(90deg, #6495ed 0%, transparent 100%); margin-bottom: 12px; width: 220px;"></div>
      <div style="font-size: 14px; color: #555; margin-bottom: 15px;">✉ ${email}</div>
      <div style="font-size: 11px; color: #333; font-style: italic;">Mobilidade • Multiproteção • Benefícios</div>
    </td>
    <td style="border-left: 2px solid #ddd; padding-left: 20px; vertical-align: middle; text-align: center;">
          <img src="https://seu-dominio.com/logo-mmb.png" alt="GRUPO MMB" style="height: 100px; width: auto;">
    </td>
  </tr>
</table>`;

  const copyToClipboard = () => {
    navigator.clipboard.writeText(htmlCode);
    setCopied(true);
    toast.success("Código HTML copiado!", {
      description: "Cole na configuração de assinatura do seu e-mail"
    });
  };

  const downloadAsImage = async () => {
    if (!signatureRef.current) return;

    const nomeArquivo = nome || "colaborador";
    const toastId = "download-image-" + Date.now();

    try {
      toast.loading("Gerando imagem...", {
        id: toastId,
        description: "Aguarde enquanto criamos sua assinatura em PNG"
      });

      // Aguardar um pouco para o toast renderizar
      await new Promise(resolve => setTimeout(resolve, 100));

      // Usar dom-to-image para capturar o preview no tamanho real
      const dataUrl = await domtoimage.toPng(signatureRef.current, {
        quality: 1,
        bgcolor: "#ffffff",
        cacheBust: true
      });

      const link = document.createElement("a");
      const filename = `assinatura_${nomeArquivo.toLowerCase().replace(/\s+/g, "_")}.png`;
      link.href = dataUrl;
      link.download = filename;
      link.style.display = "none";
      document.body.appendChild(link);
      link.click();
      
      // Aguardar antes de remover
      setTimeout(() => {
        document.body.removeChild(link);
      }, 100);

      toast.success("Imagem baixada com sucesso!", {
        id: toastId,
        description: `Arquivo: ${filename}`
      });
    } catch (error) {
      console.error("Erro ao gerar imagem:", error);
      toast.error("Erro ao gerar imagem", {
        id: toastId,
        description: "Tente novamente ou use o código HTML"
      });
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-blue-50">
      {/* Header */}
      <header className="bg-[#00203f] text-white py-6 shadow-lg">
        <div className="container flex items-center justify-center gap-3">
          <Mail className="w-8 h-8" />
          <div>
            <h1 className="text-2xl font-bold">Gerador de Assinatura de E-mail</h1>
            <p className="text-sm text-blue-200">GRUPO MMB - Mobilidade • Multiproteção • Benefícios</p>
          </div>
        </div>
      </header>

      <main className="container py-12">
        <div className="grid lg:grid-cols-2 gap-8">
          {/* Formulário */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <span>📝</span> Suas Informações
              </CardTitle>
              <CardDescription>
                Preencha seus dados para gerar sua assinatura personalizada
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="nome">Nome Completo</Label>
                <Input
                  id="nome"
                  placeholder="Ex: João Silva"
                  value={nome}
                  onChange={(e) => setNome(e.target.value)}
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="departamento">Departamento / Cargo</Label>
                <Input
                  id="departamento"
                  placeholder="Ex: Diretor Comercial"
                  value={departamento}
                  onChange={(e) => setDepartamento(e.target.value)}
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="email">E-mail</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="Ex: joao.silva@grupommb.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>

              <div className="bg-blue-50 p-4 rounded-lg border border-blue-200">
                <h3 className="font-semibold text-sm mb-2 flex items-center gap-2">
                  <span>💡</span> Como usar:
                </h3>
                <ol className="text-sm text-gray-600 space-y-1 list-decimal list-inside">
                  <li>Preencha seus dados no formulário</li>
                  <li>Veja o preview ao lado com a logo real</li>
                  <li>Baixe como imagem PNG ou copie o código HTML</li>
                  <li>Use a imagem diretamente ou cole o HTML no e-mail</li>
                </ol>
              </div>
            </CardContent>
          </Card>

          {/* Preview */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <span>👁️</span> Preview da Assinatura
              </CardTitle>
              <CardDescription>Visualização em tempo real</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              {/* Preview da Assinatura */}
              <div 
                ref={signatureRef}
                id="signature-preview"
                className="bg-white p-4 rounded-lg border-2 border-gray-200 shadow-sm"
                style={{ width: "550px", margin: "0 auto" }}
              >
                <div className="flex items-center gap-4 justify-between">
                  {/* Informações do Colaborador */}
                  <div className="flex-1">
                    <div className="text-[18px] font-bold text-[#00203f] mb-1.5">
                      {nome}
                    </div>
                    <div className="text-[14px] text-gray-700 mb-2">
                      {departamento}
                    </div>
                    <div 
                      className="h-0.5 mb-2"
                      style={{
                        background: "linear-gradient(90deg, #6495ed 0%, transparent 100%)",
                        width: "180px"
                      }}
                    />
                    <div className="text-[12px] text-gray-600 mb-2 flex items-center gap-1.5">
                      <Mail className="w-3.5 h-3.5 text-[#6495ed]" />
                      {email}
                    </div>
                    <div className="text-[10px] text-gray-600 italic">
                      Mobilidade • Multiproteção • Benefícios
                    </div>
                  </div>

                  {/* Divisória */}
                  <div className="w-0.5 h-[100px] bg-gray-300"></div>

                  {/* Logo */}
                  <div className="flex-shrink-0 flex items-center justify-center" style={{ minWidth: "120px", textAlign: "center" }}>
                    <img 
                      src="/LOGO_MMB.png" 
                      alt="GRUPO MMB" 
                      style={{ height: "75px", width: "auto", maxWidth: "100%" }}
                      crossOrigin="anonymous"
                    />
                  </div>
                </div>
              </div>

              {/* Botões de Ação */}
              <div className="grid grid-cols-2 gap-3">
                <Button
                  onClick={downloadAsImage}
                  disabled={downloading}
                  className="w-full bg-[#00203f] hover:bg-[#003366]"
                >
                  {downloading ? (
                    <>
                      <ImageIcon className="w-4 h-4 mr-2 animate-pulse" />
                      Gerando...
                    </>
                  ) : (
                    <>
                      <Download className="w-4 h-4 mr-2" />
                      Baixar PNG
                    </>
                  )}
                </Button>
                <Button
                  onClick={copyToClipboard}
                  variant="outline"
                  className="w-full border-[#00203f] text-[#00203f] hover:bg-[#00203f] hover:text-white"
                >
                  {copied ? (
                    <>
                      <CheckCircle2 className="w-4 h-4 mr-2" />
                      Copiado!
                    </>
                  ) : (
                    <>
                      <Copy className="w-4 h-4 mr-2" />
                      Copiar HTML
                    </>
                  )}
                </Button>
              </div>

              <Button
                variant="outline"
                className="w-full"
                onClick={() => {
                  const instructionsSection = document.getElementById("instructions");
                  if (instructionsSection) {
                    instructionsSection.scrollIntoView({ behavior: "smooth" });
                  }
                }}
              >
                <Download className="w-4 h-4 mr-2" />
                Ver Instruções
              </Button>
            </CardContent>
          </Card>
        </div>

        {/* Código HTML */}
        <Card className="mt-8">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <span>📄</span> Código HTML
            </CardTitle>
            <CardDescription>
              Cole este código no seu cliente de e-mail
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="relative">
              <pre className="bg-gray-50 p-4 rounded-lg overflow-x-auto text-sm border">
                <code>{htmlCode}</code>
              </pre>
              <Button
                size="sm"
                variant="ghost"
                className="absolute top-2 right-2"
                onClick={copyToClipboard}
              >
                {copied ? <CheckCircle2 className="w-4 h-4" /> : <Copy className="w-4 h-4" />}
              </Button>
            </div>
            <p className="text-sm text-amber-600 mt-4 flex items-center gap-2">
              <span>⚠️</span>
              Lembre-se de substituir a URL da imagem pela URL do logo hospedado online
            </p>
          </CardContent>
        </Card>

        {/* Guia de Configuração */}
        <Card className="mt-8">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <span>📚</span> Guia de Configuração
            </CardTitle>
            <CardDescription>
              Como adicionar a assinatura em diferentes clientes de e-mail
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid md:grid-cols-3 gap-6">
              <div>
                <h3 className="font-semibold mb-2 flex items-center gap-2">
                  <ImageIcon className="w-5 h-5 text-[#6495ed]" />
                  Usando Imagem PNG
                </h3>
                <p className="text-sm text-gray-600">
                  Clique em "Baixar PNG" e insira a imagem diretamente na configuração de assinatura.
                  Funciona em todos os clientes de e-mail.
                </p>
              </div>
              <div>
                <h3 className="font-semibold mb-2 flex items-center gap-2">
                  <Copy className="w-5 h-5 text-[#6495ed]" />
                  Usando Código HTML
                </h3>
                <p className="text-sm text-gray-600">
                  Copie o código HTML, hospede o logo online, substitua a URL e cole na configuração
                  de assinatura do seu cliente de e-mail.
                </p>
              </div>
              <div>
                <h3 className="font-semibold mb-2 flex items-center gap-2">
                  <CheckCircle2 className="w-5 h-5 text-[#6495ed]" />
                  Qual escolher?
                </h3>
                <p className="text-sm text-gray-600">
                  PNG é mais fácil e rápido. HTML oferece melhor qualidade e permite links clicáveis
                  no futuro.
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </main>

      {/* Footer */}
      <footer className="bg-[#00203f] text-white py-6 mt-12">
        <div className="container text-center">
          <p className="text-sm">
            © 2025 GRUPO MMB - Mobilidade • Multiproteção • Benefícios
          </p>
          <p className="text-xs text-blue-200 mt-2">
            Gerador de Assinatura de E-mail Profissional
          </p>
        </div>
      </footer>
    </div>
  );
}
