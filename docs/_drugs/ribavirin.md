---
layout: default
title: Ribavirin
parent: 中證據等級 (L3-L4)
nav_order: 644
evidence_level: L4
indication_count: 5
---

# Ribavirin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ribavirin：從慢性C型肝炎到慢性B型肝炎感染

## 一句話總結

Ribavirin 是一種鳥苷類似物抗病毒藥物，原本需與 Interferon 併用治療慢性C型肝炎（HCV）感染。
TxGNN 模型預測它可能對**慢性B型肝炎病毒感染 (Chronic Hepatitis B Virus Infection)** 有效，
目前雖有 **50 個臨床試驗**紀錄與 **20 篇文獻**，但經逐一核對後，證據品質有重大疑慮（詳見下方說明）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性C型肝炎（需與 Interferon 併用；香港無許可證資料可查證） |
| 預測新適應症 | 慢性B型肝炎病毒感染 (Chronic Hepatitis B Virus Infection) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L4 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）正式資料（DrugBank 查詢待補），但根據證據包中的機轉分析可以說明：Ribavirin 為鳥苷類似物，其已被臨床驗證的抗病毒效力主要針對 HCV（RNA 病毒），且必須與 Interferon 併用以誘發「突變災難 (error catastrophe)」才能發揮療效。

HBV 則是 DNA 病毒，複製途徑（經逆轉錄酶）與 HCV 完全不同，目前**沒有證據顯示 Ribavirin 對 HBV 聚合酶有直接抑制作用**。

更關鍵的是，核對本報告列出的臨床試驗標題後發現，**全部試驗設計都是「Ribavirin + Interferon 治療慢性C型肝炎」**，並非針對 HBV 單一感染的治療試驗。這很可能是 TxGNN 知識圖譜將「HBV/HCV 常見共病（co-infection）」的關聯，錯誤放大為直接適應症訊號的典型案例。真正提及 HBV 的文獻，多屬 HBV/HCV 雙重感染的治療回顧文章，屬間接證據，並非療效證據。

**結論：此預測的機轉合理性偏弱，需視為需要進一步驗證的研究假說，而非有實證支持的候選適應症。**

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00215865](https://clinicaltrials.gov/study/NCT00215865) | Phase 3 | 完成 | 600 | PEGIntron+Ribavirin 治療慢性C型肝炎（非HBV）；相關性評級 C——僅示範藥物合併使用安全性背景，與 HBV 無直接關聯 |
| [NCT00940420](https://clinicaltrials.gov/study/NCT00940420) | Phase 4 | 完成 | 2695 | Peginterferon alfa (Pegasys) + Ribavirin (Copegus) 用於慢性C型肝炎之安全性/耐受性研究，非 HBV |
| [NCT00265395](https://clinicaltrials.gov/study/NCT00265395) | Phase 3 | 完成 | 1428 | PEG-Intron + Rebetol 治療 Genotype 1 慢性C型肝炎，非 HBV |
| [NCT01598090](https://clinicaltrials.gov/study/NCT01598090) | Phase 3 | 完成 | 881 | Peginterferon Lambda-1a/Alfa-2a + Ribavirin + Telaprevir 治療 HCV Genotype 1；相關性評級 C——受試族群為 HCV 感染者，非 HBV，不能作為 HBV 適應症直接證據 |
| [NCT01937728](https://clinicaltrials.gov/study/NCT01937728) | Phase 4 | 完成 | 542 | Peginterferon Alfa-2a + Ribavirin 依病毒動力學調整療程，用於 Genotype 1 慢性C型肝炎 |
| [NCT00086541](https://clinicaltrials.gov/study/NCT00086541) | Phase 3 | 完成 | 515 | Interferon Alfacon-1 + Ribavirin 用於 Peg-IFN/Ribavirin 治療無反應之慢性C型肝炎患者 |
| [NCT02332720](https://clinicaltrials.gov/study/NCT02332720) | Phase 2 | 完成 | 413 | Grazoprevir/Uprifosbuvir 併用/不併用 Ribavirin，治療 HCV Genotype 3-6 |
| [NCT01220947](https://clinicaltrials.gov/study/NCT01220947) | Phase 2 | 完成 | 421 | Danoprevir/Ritonavir + Pegasys/Copegus 治療初治慢性C型肝炎；相關性評級 C——非 HBV 適應症證據 |
| [NCT01854697](https://clinicaltrials.gov/study/NCT01854697) | Phase 3 | 完成 | 311 | ABT-450/r/ABT-267+ABT-333 併用/不併用 Ribavirin 對比 Telaprevir，治療 HCV Genotype 1 |
| [NCT01830127](https://clinicaltrials.gov/study/NCT01830127) | Phase 2 | 完成 | 35 | BI 207127+Faldaprevir+Ribavirin 治療中度肝功能不全之 HCV Genotype 1b 患者；相關性評級 C——與 HBV 無關 |

**注意：以上試驗全數以 HCV（C型肝炎）患者為受試對象，未發現任何直接針對 HBV 單一感染設計的試驗。**

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV 共感染治療回顧，建議 PEG-IFN+Ribavirin 用於共感染中 HCV RNA 陽性者，非單獨 HBV 適應症 |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | 雙重 HCV/HBV 感染治療與預後更新，強調需依病毒活性決定治療策略 |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Cohort | Current Opinion in Virology | IL28B 基因型對 HBV 與 HCV 感染治療反應的影響（HCV 為主要治療標的） |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World J Gastroenterol | HBV/HCV 化療/免疫治療綜述，指出 HCV 可經 DAA 清除，HBV 仍需長期治療 |
| [21538279](https://pubmed.ncbi.nlm.nih.gov/21538279/) | 2011 | Review | Seminars in Liver Disease | 慢性 HBV/HCV 宿主基因學回顧 |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatology International | 雙重慢性 HBV/HCV 感染回顧，討論病毒交互作用機轉 |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | Journal of Hepatology | HBV/HCV 共感染治療挑戰（摘要資料不完整） |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | 未分類 | World J Gastroenterol | IL28B 基因多型性與 HBV 感染關聯，主要證據仍來自 HCV 治療反應研究 |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | 未分類 | Expert Rev Anti Infect Ther | 兒童慢性 HBV/HCV 治療選項綜述 |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | 未分類 | World J Gastroenterol | 慢性 HBV/HCV 感染之肝細胞癌預防策略回顧 |

**注意：無任何 RCT 直接支持 Ribavirin 對 HBV 的療效；現有文獻多為 HBV/HCV 共感染的回顧性論述。**

---

## 香港上市資訊

目前 Ribavirin 未在香港上市（`market_status: 未上市`），查無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 現有 50 個臨床試驗與 20 篇文獻中，實際受試對象幾乎全為 HCV 感染者，並非 HBV 直接證據；機轉分析亦指出 HBV（DNA病毒）與 Ribavirin 已知抗病毒機轉（針對 RNA 病毒的突變災難效應）不吻合。
- 此預測很可能源自 TxGNN 知識圖譜對「HBV/HCV 常見共病」關聯的錯誤放大，而非真實藥理訊號。

**若要推進需要：**
- 補齊 TFDA/仿單警語與禁忌症資料（DG001，Blocking，來源：TFDA 官網仿單 PDF）
- 補齊完整 MOA 資料（DG002，High，來源：DrugBank API）
- 若欲繼續驗證，需針對 HBV（而非 HCV）設計專屬體外/體內機轉研究，確認 Ribavirin 是否對 HBV 複製有直接抑制作用
- 在缺乏直接 HBV 證據前，不建議投入後續資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

