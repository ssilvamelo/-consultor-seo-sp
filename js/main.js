/**
 * Consultor SEO SP — Scripts Interativos (v2.5 Pro)
 * Simulador de Diagnóstico de IA & SEO, FAQ Accordion e Integração WhatsApp
 */

document.addEventListener("DOMContentLoaded", function () {
  // 1. FAQ Accordion Toggle
  const faqButtons = document.querySelectorAll(".faq-question");
  faqButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      const item = this.parentElement;
      const isOpen = item.classList.contains("active");

      // Fecha todos os outros itens
      document.querySelectorAll(".faq-item").forEach((fi) => fi.classList.remove("active"));

      if (!isOpen) {
        item.classList.add("active");
      }
    });
  });

  // 2. Simulador Interativo de Diagnóstico de IA & SEO
  const simSetor = document.getElementById("sim-setor");
  const simNivel = document.getElementById("sim-nivel");
  const simMeta = document.getElementById("sim-meta");
  const resultMetric = document.getElementById("result-metric");
  const resultExplanation = document.getElementById("result-explanation");
  const btnSendWhatsapp = document.getElementById("btn-send-whatsapp");

  function calculateSimulation() {
    if (!simSetor || !simNivel || !simMeta) return;

    const setor = simSetor.value;
    const nivel = simNivel.value;
    const meta = simMeta.value;

    let multiplier = "5.8x";
    let text = "Implementação recomendada: Arquitetura de autoridade tópica com plataforma própria de alta velocidade + agentes autônomos para triagem e qualificação de oportunidades.";

    if (nivel === "novo") {
      multiplier = "10.4x";
      text = "Aceleração imediata de posicionamento com foco em intenção de compra, infraestrutura de carregamento instantâneo e captação ativa de clientes qualificados.";
    } else if (nivel === "estagnado") {
      multiplier = "7.2x";
      text = "Reestruturação estratégica de conteúdo em silos, eliminação de gargalos técnicos de plataformas antigas e foco cirúrgico em conversão de vendas.";
    } else if (nivel === "avancado") {
      multiplier = "4.5x";
      text = "Desenvolvimento de ecossistema com agentes autônomos para automação de processos internos, central de inteligência privada e escala de vendas 24/7.";
    }

    if (meta === "leads") {
      multiplier += " Leads";
    } else if (meta === "automacao") {
      multiplier += " Eficiência";
    } else {
      multiplier += " Autoridade";
    }

    if (resultMetric) resultMetric.textContent = multiplier;
    if (resultExplanation) resultExplanation.textContent = text;

    // Atualiza o link do botão de WhatsApp
    if (btnSendWhatsapp) {
      const msg = encodeURIComponent(
        `Olá! Realizei o diagnóstico no site consultorseosp.com.br:\n` +
        `• Setor: ${setor}\n` +
        `• Situação Atual: ${nivel}\n` +
        `• Objetivo Principal: ${meta}\n` +
        `Gostaria de agendar uma reunião técnica para analisar esse plano de implementação.`
      );
      btnSendWhatsapp.href = `https://wa.me/5511918738164?text=${msg}`;
    }
  }

  if (simSetor && simNivel && simMeta) {
    simSetor.addEventListener("change", calculateSimulation);
    simNivel.addEventListener("change", calculateSimulation);
    simMeta.addEventListener("change", calculateSimulation);
    calculateSimulation();
  }
});
