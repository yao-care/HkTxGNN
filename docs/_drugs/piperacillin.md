---
layout: default
title: Piperacillin
parent: 僅模型預測 (L5)
nav_order: 704
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Piperacillin：預測新適應症為類風濕性關節炎 (Rheumatoid Arthritis)（證據等級 L5）。原適應症：目前缺乏核准適應症文字（請參考原廠仿單）"
monitor_inn: "PIPERACILLIN"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "sclerosing cholangitis", "osteoarthritis susceptibility"]
---

# Piperacillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Piperacillin：從細菌感染到類風濕性關節炎

## 一句話總結

Piperacillin 是 β-內醯胺類（青黴素類）抗生素，在香港多以與 tazobactam 的複方注射劑上市，用於細菌感染治療。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，但目前**沒有任何臨床試驗**，檢索到的文獻也只是把 RA 當成病患背景，**沒有實質證據**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前缺乏核准適應症文字（請參考原廠仿單） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理知識，Piperacillin 是 β-內醯胺類抗生素，透過結合青黴素結合蛋白 (PBP) 抑制細菌細胞壁合成，用於細菌感染。

類風濕性關節炎是自體免疫疾病，核心病理是免疫失調與慢性滑膜發炎。Piperacillin 沒有已知的抗發炎或免疫調節作用，與 RA 的病理機轉缺乏可信的關聯。

因此，0.999 的 TxGNN 分數僅是模型預測，不具藥理學上的支持。檢索到的文獻中，RA 只是病患背景：這些病例是免疫抑制的 RA 患者發生感染，並以 piperacillin/tazobactam 治療感染，並未顯示對 RA 本身有療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表僅列出與藥物或 RA 背景較相關的文獻。這些文獻均為病例報告或觀察性研究，**沒有任何一篇顯示 piperacillin 對 RA 有治療效果**。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Ann Transl Med | 抗生素相關藥物性肝損傷的盛行率與臨床特徵 |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2026 | Cohort（預測模型） | Br J Clin Pharmacol | 建立 ampicillin/sulbactam 或 piperacillin/tazobactam 治療者發生嗜酸性球增多的預測模型 |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case report | Orthopadie | RA 患者人工膝關節的流感嗜血桿菌感染，曾以 piperacillin/tazobactam 治療肺炎 |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case report | BMJ Case Rep | RA 患者使用 etanercept 後發生化膿性心包炎，經驗性使用 piperacillin-tazobactam |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Case report | Front Immunol | 長期免疫抑制的 RA 患者發生大腸桿菌引起的非典型丹毒與敗血性休克 |
| [40119266](https://pubmed.ncbi.nlm.nih.gov/40119266/) | 2025 | Case report/Review | BMC Infect Dis | 抗藥性 Edwardsiella tarda 引起的敗血性休克 |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case report | Proc (Bayl Univ Med Cent) | RA 患者低劑量 methotrexate 毒性導致全血球減少，以 leucovorin 解救（與 piperacillin 無關） |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case report | Cureus | 低劑量 methotrexate 導致全血球減少（與 piperacillin 無關） |

---

## 香港上市資訊

香港共有 14 張有效許可證，皆為單一成分登記（含與 tazobactam 的組合製劑產品）。資料中未提供劑型與核准適應症文字。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58094 | TAZOCIN FOR INJ 4.5G（輝瑞） | 注射劑 | 請參考原廠仿單 |
| HK-49703 | TAZOCIN FOR INJ 4.5G（輝瑞） | 注射劑 | 請參考原廠仿單 |
| HK-60314 | PYBACTAM 4.5G POWDER FOR SOLN FOR INJ/INF（Sandoz） | 注射／輸注用粉劑 | 請參考原廠仿單 |
| HK-65419 | PIPERACILLIN/TAZOBACTAM KABI 4G/0.5G（Fresenius Kabi） | 輸注用粉劑 | 請參考原廠仿單 |
| HK-56958 | PIPERACILLIN SODIUM FOR INJ. 4G（Jindun） | 注射劑 | 請參考原廠仿單 |

---

## 安全性考量

- **藥物交互作用**：共查得 81 筆交互作用，以下為其中較重要者：
  - **重大 (Major)**：Vancomycin
  - **中度 (Moderate)**：Doxycycline、Tetracycline、Minocycline、Kanamycin、Streptomycin、Picosulfuric acid
  - **輕微 (Minor)**：Clarithromycin
- **文獻提示的風險**：檢索文獻提到抗生素相關藥物性肝損傷，以及 piperacillin/tazobactam 治療者可能發生嗜酸性球增多。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測僅來自模型分數，沒有臨床試驗，文獻也僅把 RA 當作感染病例的背景，無法顯示 piperacillin 對 RA 有療效。
- Piperacillin 是抗菌藥，沒有已知的抗發炎或免疫調節機轉，且 RA 已有成熟的標準治療。

**若要推進需要：**
- 提出可信的作用機轉假說（例如抗發炎或免疫調節活性）並以前臨床實驗驗證
- 取得香港原廠仿單的核准適應症、警語與禁忌症，以完成安全性評估
- 在沒有上述證據前，不建議投入臨床開發資源

---

### 其他預測適應症（供參考）

其餘 TxGNN 預測同樣僅有模型分數，均為 L5、建議 Hold：

| 預測適應症 | TxGNN 分數 | 說明 |
|-----------|-----------|------|
| 脈絡膜缺損性小眼症－肢根型發育不良症候群 | 99.89% | 罕見發育性遺傳疾病，抗菌藥無合理機轉，無試驗與文獻 |
| 短指併指症候群 | 99.86% | 先天性肢體畸形，無機轉關聯，無試驗與文獻 |
| 硬化性膽管炎 | 99.82% | 僅有腸道菌叢假說等間接推測；piperacillin 另與藥物性肝損傷相關，不利膽汁淤積性疾病 |
| 骨關節炎易感性 | 99.56% | 檢索到的唯一文獻是 linezolid 與 vancomycin 比較，與 piperacillin 及骨關節炎治療均無關 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

