---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
---

# Metronidazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Metronidazole：從厭氧菌與原蟲感染到肺囊蟲症

## 一句話總結

Metronidazole 是硝基咪唑類抗微生物藥，用於厭氧菌與原蟲感染。
TxGNN 模型預測它可能對**肺囊蟲症 (Pneumocystosis)** 有效，但目前**沒有任何相關臨床試驗**，也沒有直接支持療效的文獻。這個預測在機轉上缺乏依據，較像是知識圖譜的統計假象。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症文字（依藥理屬抗厭氧菌／抗原蟲感染藥） |
| 預測新適應症 | 肺囊蟲症 (Pneumocystosis) |
| TxGNN 預測分數 | 99.99%（模型排名 435） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

**這個預測目前並不合理。** 目前缺乏詳細的作用機轉資料。已知 Metronidazole 的硝基會在厭氧菌與原蟲體內被還原活化，因而產生殺菌作用。

肺囊蟲（Pneumocystis）屬於真菌，並非硝基咪唑類的已知作用對象。肺囊蟲肺炎的標準治療是 TMP-SMX（trimethoprim-sulfamethoxazole）。檢索到的文獻中，只有一篇 1980 年的綜述提到這一點，同時把 Metronidazole 列為阿米巴痢疾與滴蟲症用藥。

0.9999 的高分很可能來自藥物在圖譜中位於抗微生物藥的鄰近區域，不代表實際療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

系統以關鍵字比對到 23 筆試驗，經逐筆審視，內容都與 Metronidazole 或肺囊蟲無關（例如頭頸癌存活者照護工具、鴉片類藥物風險降低、糖尿病衛教、初級照護給付模式等）。其中雖有標示 Phase 3 者，實際是衛教或照護模式研究，不能作為藥物證據，也不應提升證據等級。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | 抗寄生蟲藥物綜述，談抗藥性、藥物可得性與特殊族群使用限制 |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Metronidazole 用於阿米巴結腸炎與滴蟲症；肺囊蟲肺炎首選是 TMP-SMX |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | 抗原蟲治療的藥物動力學依據與美國用藥建議 |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV 相關伺機性感染現況，未提及 Metronidazole 用於肺囊蟲 |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | AIDS 感染併發症治療綜述，肺囊蟲肺炎為最常見的致命感染 |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | 抗微生物預防性用藥試驗的評析，與肺囊蟲無直接關聯 |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | 人類原蟲感染用藥綜述（無摘要） |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | 病人先因腹瀉接受 Metronidazole 與四環素，之後才發生肺囊蟲與巨細胞病毒肺炎，屬先後出現，非治療證據 |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | AIDS 病人以 Metronidazole 治療阿米巴痢疾，之後發生肺囊蟲肺炎，非治療證據 |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | AIDS 病人併發巨細胞病毒與阿米巴結腸炎、結腸穿孔，與肺囊蟲療效無關 |

這些文獻多是「同一批病人同時出現這些疾病」或「Metronidazole 用於其他感染」，沒有任何一篇顯示它對肺囊蟲有效。

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張（資料庫未載明劑型與核准適應症）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-36789 | METRONIDAZOLE CAP 200MG | 未載明 | 未載明 |
| HK-52934 | PHARMANIAGA METRONIDAZOLE TAB 200MG | 未載明 | 未載明 |
| HK-66809 | METROMILL SOLUTION FOR INFUSION 500MG/100ML | 未載明 | 未載明 |
| HK-31381 | VAGICIN TAB 200MG | 未載明 | 未載明 |
| HK-34348 | METRONIL CAP 200MG | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。DrugBank 查無藥物交互作用紀錄。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測（肺囊蟲症）缺乏機轉依據與實際研究，且標準治療（TMP-SMX）明確，不建議投入資源。
- 其他預測中，**Cap polyposis** 的訊號相對最可信（L4，列為研究問題）。它與腸道菌叢失衡有關，文獻提出 Metronidazole 可能透過抗菌或抗發炎作用起效，但目前僅有病例報告，且緩解常出現在多種抗生素合併使用之後，無法單獨歸因。
- **潰瘍性直腸乙狀結腸炎**與**外陰潰瘍**同為 L4：前者文獻只有 IBD 綜述與相關病例，後者只有阿米巴感染等病因明確的個案。

**若要推進需要：**
- 補齊香港衞生署仿單的警語與禁忌資料（DG001，屬阻擋項）與 DrugBank 的作用機轉（DG002）。
- 若研究方向改為 Cap polyposis，先做針對性的全文回顧，釐清 Metronidazole 單獨的貢獻，再評估是否設計前瞻性研究。
- 對外陰潰瘍，須逐篇確認 Metronidazole 特有的結果，才可能升至 L3。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選須經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

