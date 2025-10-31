import { useState, useRef } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { Copy, Download, Mail, CheckCircle2, Image as ImageIcon } from "lucide-react";
import { toast } from "sonner";
import domtoimage from "dom-to-image";

export default function Home() {
  // Estado da empresa selecionada
  const [selectedCompany, setSelectedCompany] = useState<'mmb' | 'alpha'>('mmb');

  // Estados do formulário
  const [nome, setNome] = useState("Nome do Colaborador");
  const [departamento, setDepartamento] = useState("Departamento do Colaborador");
  const [email, setEmail] = useState("email@grupommb.com");
  const [telefone, setTelefone] = useState("");
  const [copied, setCopied] = useState(false);
  const [downloading, setDownloading] = useState(false);
  const signatureRef = useRef<HTMLDivElement>(null);

  // Função para gerar código HTML do MMB
  const generateMMBHtmlCode = () => {
    const telefoneLine = telefone ? `<div style="font-size: 14px; color: #555; margin-bottom: 8px;">📱 ${telefone}</div>` : '';
    
    return `<table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, sans-serif; max-width: 650px;">
  <tr>
    <td style="padding-right: 20px; vertical-align: middle;">
      <div style="font-size: 22px; font-weight: bold; color: #00203f; margin-bottom: 8px;">${nome}</div>
      <div style="font-size: 16px; color: #444; margin-bottom: 12px;">${departamento}</div>
      <div style="height: 2px; background: linear-gradient(90deg, #6495ed 0%, transparent 100%); margin-bottom: 12px; width: 220px;"></div>
      <div style="font-size: 14px; color: #555; margin-bottom: 8px;">✉ ${email}</div>
      ${telefoneLine}
      <div style="font-size: 11px; color: #333; font-style: italic; font-weight: 500;">Mobilidade • Multiproteção • Benefícios</div>
    </td>
    <td style="border-left: 3px solid #6495ed; padding-left: 20px; vertical-align: middle; text-align: center;">
      <img src="https://seu-dominio.com/logo-mmb.png" alt="GRUPO MMB" style="height: 100px; width: auto;">
    </td>
  </tr>
</table>`;
  };

  // Função para gerar código HTML da Alpha
  const generateAlphaHtmlCode = () => {
    const telefoneLine = telefone ? `<div style="font-size: 14px; color: #555; margin-bottom: 8px;">📱 ${telefone}</div>` : '';
    
    return `<table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, sans-serif; max-width: 650px;">
  <tr>
    <td style="padding-right: 20px; vertical-align: middle; text-align: center;">
      <img src="https://seu-dominio.com/logo-alpha.png" alt="ALPHA PROTEÇÕES" style="height: 100px; width: auto;">
    </td>
    <td style="border-left: 3px solid #1E5BA8; padding-left: 20px; vertical-align: middle;">
      <div style="font-size: 22px; font-weight: bold; color: #1E5BA8; margin-bottom: 8px;">${nome}</div>
      <div style="font-size: 16px; color: #444; margin-bottom: 12px;">${departamento}</div>
      <div style="height: 2px; background: linear-gradient(90deg, #1E5BA8 0%, transparent 100%); margin-bottom: 12px; width: 220px;"></div>
      <div style="font-size: 14px; color: #555; margin-bottom: 8px;">✉ ${email}</div>
      ${telefoneLine}
    </td>
  </tr>
</table>`;
  };

  const htmlCode = selectedCompany === 'mmb' ? generateMMBHtmlCode() : generateAlphaHtmlCode();

  const copyToClipboard = () => {
    navigator.clipboard.writeText(htmlCode);
    setCopied(true);
    toast.success("Código HTML copiado!", {
      description: "Cole na configuração de assinatura do seu e-mail"
    });
    setTimeout(() => setCopied(false), 2000);
  };

  const downloadAsImage = async () => {
    if (!signatureRef.current) return;

    const nomeArquivo = nome || "colaborador";
    const toastId = "download-image-" + Date.now();

    try {
      setDownloading(true);
      toast.loading("Gerando imagem...", {
        id: toastId,
        description: "Aguarde enquanto criamos sua assinatura em PNG"
      });

      await new Promise(resolve => setTimeout(resolve, 100));

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
    } finally {
      setDownloading(false);
    }
  };

  const headerColor = selectedCompany === 'mmb' ? '#00203f' : '#1E5BA8';
  const accentColor = selectedCompany === 'mmb' ? '#6495ed' : '#1E5BA8';
  const companyName = selectedCompany === 'mmb' ? 'GRUPO MMB' : 'ALPHA PROTEÇÕES';
  const companyTagline = selectedCompany === 'mmb' ? 'Mobilidade • Multiproteção • Benefícios' : 'Proteções e Segurança';
  const logoSrc = selectedCompany === 'mmb' ? '/LOGO_MMB.png' : '/LOGO_ALPHA.png';
  const emailPlaceholder = selectedCompany === 'mmb' ? 'Ex: joao.silva@grupommb.com' : 'Ex: junio.tosta@alphanacional.com.br';

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-blue-50">
      {/* Header */}
      <header className="text-white py-6 shadow-lg" style={{ backgroundColor: headerColor }}>
        <div className="container flex items-center justify-center gap-3">
          <Mail className="w-8 h-8" />
          <div>
            <h1 className="text-2xl font-bold">Gerador de Assinatura de E-mail</h1>
            <p className="text-sm opacity-90">{companyName} - {companyTagline}</p>
          </div>
        </div>
      </header>

      <main className="container py-12">
        {/* Seletor de Empresa */}
        <Card className="mb-8">
          <CardHeader>
            <CardTitle>Selecione a Empresa</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex gap-4">
              <Button
                onClick={() => setSelectedCompany('mmb')}
                className={`flex-1 ${selectedCompany === 'mmb' ? 'bg-[#00203f] text-white' : 'bg-gray-200 text-gray-800'}`}
              >
                GRUPO MMB
              </Button>
              <Button
                onClick={() => setSelectedCompany('alpha')}
                className={`flex-1 ${selectedCompany === 'alpha' ? 'bg-[#1E5BA8] text-white' : 'bg-gray-200 text-gray-800'}`}
              >
                ALPHA PROTEÇÕES
              </Button>
            </div>
          </CardContent>
        </Card>

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
                  placeholder={emailPlaceholder}
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="telefone">Telefone (Opcional)</Label>
                <Input
                  id="telefone"
                  placeholder="Ex: (11) 98765-4321"
                  value={telefone}
                  onChange={(e) => setTelefone(e.target.value)}
                />
              </div>

              <div className="bg-blue-50 p-4 rounded-lg border border-blue-200">
                <h3 className="font-semibold text-sm mb-2 flex items-center gap-2">
                  <span>💡</span> Como usar:
                </h3>
                <ol className="text-sm text-gray-600 space-y-1 list-decimal list-inside">
                  <li>Selecione a empresa desejada</li>
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
                className="bg-white rounded-lg border-2 border-gray-200 shadow-sm"
                style={{ width: "650px", margin: "0 auto" }}
              >
                <div className="flex items-center justify-center gap-4 p-4">
                  {selectedCompany === 'mmb' ? (
                    <>
                      {/* Informações do Colaborador (MMB) */}
                      <div className="flex-1 max-w-[350px]">
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
                        {telefone && (
                          <div className="text-[12px] text-gray-600 mb-2">
                            📱 {telefone}
                          </div>
                        )}
                        <div className="text-[10px] text-gray-600 italic">
                          Mobilidade • Multiproteção • Benefícios
                        </div>
                      </div>

                      {/* Divisória */}
                      <div className="w-1 h-[80px] bg-[#6495ed] mx-6"></div>

                      {/* Logo MMB */}
                      <div className="flex-shrink-0 flex items-center justify-center" style={{ width: "180px", textAlign: "center" }}>
                        <img 
                          src={logoSrc}
                          alt="GRUPO MMB" 
                          style={{ height: "75px", width: "auto", maxWidth: "100%" }}
                          crossOrigin="anonymous"
                        />
                      </div>
                    </>
                  ) : (
                    <>
                      {/* Logo Alpha */}
                      <div className="flex-shrink-0 flex items-center justify-center" style={{ width: "180px", textAlign: "center" }}>
                        <img 
                          src={logoSrc}
                          alt="ALPHA PROTEÇÕES" 
                          style={{ height: "75px", width: "auto", maxWidth: "100%" }}
                          crossOrigin="anonymous"
                        />
                      </div>

                      {/* Divisória */}
                      <div className="w-1 h-[80px] bg-[#1E5BA8] mx-6"></div>

                      {/* Informações do Colaborador (Alpha) */}
                      <div className="flex-1 max-w-[350px]">
                        <div className="text-[18px] font-bold text-[#1E5BA8] mb-1.5">
                          {nome}
                        </div>
                        <div className="text-[14px] text-gray-700 mb-2">
                          {departamento}
                        </div>
                        <div 
                          className="h-0.5 mb-2"
                          style={{
                            background: "linear-gradient(90deg, #1E5BA8 0%, transparent 100%)",
                            width: "180px"
                          }}
                        />
                        <div className="text-[12px] text-gray-600 mb-2 flex items-center gap-1.5">
                          <Mail className="w-3.5 h-3.5 text-[#1E5BA8]" />
                          {email}
                        </div>
                        {telefone && (
                          <div className="text-[12px] text-gray-600 mb-2">
                            📱 {telefone}
                          </div>
                        )}
                      </div>
                    </>
                  )}
                </div>
              </div>

              {/* Botões de Ação */}
              <div className="grid grid-cols-2 gap-3">
                <Button
                  onClick={downloadAsImage}
                  disabled={downloading}
                  className="w-full text-white"
                  style={{ backgroundColor: headerColor }}
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
                  className="w-full"
                  style={{ borderColor: headerColor, color: headerColor }}
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
            </div>
          </CardContent>
        </Card>
      </main>
    </div>
  );
}

