---
layout: default
title: Clobetasol
parent: 中證據等級 (L3-L4)
nav_order: 182
evidence_level: L3
indication_count: 1
---

# Clobetasol
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Clobetasol：從皮膚炎症到原發性皮膚T細胞淋巴瘤

## 一句話總結

Clobetasol propionate 是 Class I 超強效外用糖皮質激素，原本廣泛用於各類炎症性皮膚病（如銀屑病、濕疹、皮炎）的治療。
TxGNN 模型預測它可能對**原發性皮膚T細胞淋巴瘤 (Primary Cutaneous T-Cell Lymphoma)** 有效，
目前有 **0 個臨床試驗**和 **20 篇文獻**（其中多篇直接涉及 Clobetasol 用於蕈樣黴菌病）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 炎症性皮膚病（外用超強效糖皮質激素） |
| 預測新適應症 | 原發性皮膚T細胞淋巴瘤 (Primary Cutaneous T-Cell Lymphoma) |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Clobetasol propionate 為 Class I 超強效外用糖皮質激素，其與原發性皮膚T細胞淋巴瘤（CTCL）治療的機轉關聯性可從三個層面理解：

**直接淋巴細胞毒性**：糖皮質激素受體（Glucocorticoid Receptor, GR）在 T 淋巴細胞中廣泛表達，GR 活化後可上調 BIM、PUMA 等促凋亡基因，直接誘導腫瘤性 T 細胞凋亡，達到局部腫瘤清除效果。

**腫瘤微環境調節**：CTCL（尤其是進展期）常出現 Th2 細胞因子偏移，包括 IL-2、IL-4、IL-5、IL-13 過量分泌。Clobetasol 能有效抑制上述細胞因子，降低腫瘤促進性炎症，改善腫瘤微環境。

**與現有指引一致**：此機轉與 NCCN 及 EORTC 指引將外用強效糖皮質激素列為早期蕈樣黴菌病（Mycosis Fungoides, MF，IA–IIA 期）一線治療方案的臨床依據高度吻合。事實上，多篇文獻已直接報告 Clobetasol propionate 0.05% 用於早期 MF 的有效性（反應率逾 90%），TxGNN 預測結果與既有臨床實踐具高度一致性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [39741016](https://pubmed.ncbi.nlm.nih.gov/39741016/) | 2025 | 比較研究 | Anais brasileiros de dermatologia | 比較 Clobetasol propionate 與 Bexarotene 用於早期 MF 的療效，直接對照兩種一線外用療法 |
| [32603400](https://pubmed.ncbi.nlm.nih.gov/32603400/) | 2020 | 回溯性世代研究 | Cutis | Clobetasol propionate 0.05% 乳膏用於早期 MF 患者的療效與皮膚副作用觀察，療效佳且副作用輕微 |
| [14686970](https://pubmed.ncbi.nlm.nih.gov/14686970/) | 2003 | 臨床經驗回顧 | Dermatologic Therapy | UCSF 約 200 例 patch 期 MF 以高效外用類固醇（以 Clobetasol 為主）治療，反應率逾 90%，被列為早期 MF 一線方案 |
| [25027222](https://pubmed.ncbi.nlm.nih.gov/25027222/) | 2014 | 病例報告 | Nederlands tijdschrift voor geneeskunde | 9 歲女童低色素型 MF，以 Clobetasol 0.05% 軟膏每週 4 天治療後皮損成功消退 |
| [28804923](https://pubmed.ncbi.nlm.nih.gov/28804923/) | 2017 | 病例報告 | Pediatric Dermatology | 兒童低色素型 MF 合併大細胞轉化，Clobetasol 治療後有初步反應，同時探討診斷與治療挑戰 |
| [28031140](https://pubmed.ncbi.nlm.nih.gov/28031140/) | 2016 | 病例系列 | Skinmed | 血管免疫母細胞性 T 細胞淋巴瘤之皮膚表現，患者初誤診為銀屑病並以 Clobetasol 乳膏治療，病情惡化後確診，提示 CTCL 的鑑別診斷重要性 |
| [30677799](https://pubmed.ncbi.nlm.nih.gov/30677799/) | 2018 | 綜述文章 | Dermatology Online Journal | Lymphomatoid papulosis（低度惡性 CTCL 變體）的臨床診治回顧，探討其與 CTCL 的關係及監測策略 |
| [17083888](https://pubmed.ncbi.nlm.nih.gov/17083888/) | 2006 | 綜述文章 | Dermatology Online Journal | CD30+ 大細胞 T 細胞淋巴瘤的診斷鑑別與治療原則，強調組織病理確認對 CTCL 亞型分類的重要性 |
| [36846176](https://pubmed.ncbi.nlm.nih.gov/36846176/) | 2023 | 病例報告及文獻回顧 | Clinical Case Reports | MF 呈銀屑病樣皮損，初以外用類固醇治療 12 年仍惡化，最終確診 MF，強調 MF 誤診問題 |
| [33026773](https://pubmed.ncbi.nlm.nih.gov/33026773/) | 2020 | 病例報告 | Journal of Drugs in Dermatology | 持續性聚集型 CD30+ 淋巴增殖性疾病（LyP 亞型），探討其良性病程與 CTCL 的鑑別及處置 |

---

## 香港上市資訊

Clobetasol 目前在香港**未有已登記許可證**，無法提供上市品項資料。

如需臨床應用，需透過特別進口申請（Special Purpose Import）或參考其他已上市地區（如英國、美國）的核准仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
雖無已登記的臨床試驗，但現有文獻（包括多篇直接使用 Clobetasol 治療早期 MF 的觀察性研究）顯示強烈的機轉合理性與初步臨床佐證，且 NCCN/EORTC 指引亦支持外用強效糖皮質激素作為早期 MF 一線治療。TxGNN 預測結果（99.51%）與現行臨床實踐高度吻合，具備進一步評估的充分依據。

**若要推進需要：**
- 取得香港衛生署特別進口許可或確認海外供貨鏈，因香港目前無已登記許可證
- 補充完整的安全性資料：TFDA 或 EMA/FDA 仿單警語、禁忌症及藥物交互作用
- 確認詳細作用機轉（MOA）資料（目前為 Data Gap），以強化機轉關聯性分析
- 針對 CTCL 患者族群（免疫功能可能受損）制定皮膚副作用監測計畫（皮膚萎縮、毛囊炎、HPA 軸抑制等）
- 考慮啟動前瞻性觀察性研究或參與多中心 IIT（Investigator-Initiated Trial），以建立 Phase 2 等級的療效證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

