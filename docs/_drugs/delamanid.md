---
layout: default
title: Delamanid
parent: 中證據等級 (L3-L4)
nav_order: 249
evidence_level: L4
indication_count: 10
---

# Delamanid
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Delamanid：從多重抗藥性結核病到牛型結核病

## 一句話總結

Delamanid 是硝基二氫咪唑并噁唑類（nitro-dihydro-imidazooxazole）抗結核藥，原本用於多重抗藥性結核病（MDR-TB）。
TxGNN 模型預測它可能對**牛型結核病 (Tuberculosis, bovine)** 有效，但這個預測目前只有 **0 個臨床試驗**和 **1 篇間接文獻**支持。
同一批預測中，「非活動性結核病」的證據明顯較強（2 個進行中的臨床試驗），詳見結論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 牛型結核病 (Tuberculosis, bovine) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

註：香港許可證資料未列載核准適應症，原適應症「多重抗藥性結核病」是依一般藥理知識與 Evidence Pack 的機轉說明判斷，並非來自許可證欄位。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。以下說明來自一般藥理知識，並非來自提供的資料。Delamanid 需經分枝桿菌的 F420 依賴性酶活化，再抑制黴菌酸（mycolic acid）合成，進而殺死結核分枝桿菌，包括部分抗藥株。

牛型結核病由牛分枝桿菌（*M. bovis*）引起，屬於結核分枝桿菌複合群（MTBC），與人類結核病的病原體同屬一群。因此 delamanid 在機轉上有可能有效。模型的高分很可能反映了知識圖譜中「結核病」相關節點彼此接近。

不過，目前沒有任何 delamanid 針對 *M. bovis* 的專屬數據。此預測應視為待驗證的研究問題，而不是有實證支持的新適應症。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | 分子流行病學／抗藥性調查 | BMC Genomics | 用全基因體定序分析人類人畜共通結核病中 *M. bovis* 分離株的基因型、毒力與抗藥性特徵；摘要未提及 delamanid |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64412 | DELTYBA TABLETS 50MG（廠商：OTSUKA PHARMACEUTICAL (H.K.) LIMITED） | 片劑（依品名判斷） | 許可證資料未列載 |

## 安全性考量

安全性資訊請參考原廠仿單。DrugBank 查無藥物交互作用紀錄。

## 結論與下一步

**決策：Hold**

**理由：**
- 「牛型結核病」目前只有模型分數和一篇與 delamanid 無直接關聯的基因體研究，沒有任何 delamanid 對 *M. bovis* 的證據，因此列為研究問題。
- 同批預測中，**非活動性結核病 (inactive tuberculosis)** 證據較強（L2，建議 Proceed with Guardrails）。它有兩個進行中的試驗，都尚無結果：
  - [NCT03568383](https://clinicaltrials.gov/study/NCT03568383)（PHOENIx，Phase 3，n=5,832）：在 MDR-TB 患者的高風險家戶接觸者中，比較 delamanid 與 isoniazid 預防活動性結核病的效果。
  - [NCT05766267](https://clinicaltrials.gov/study/NCT05766267)（CRUSH-TB，Phase 2/3，n=288）：評估肺結核短程療程，與非活動性結核病的相關性較弱。
- 其餘預測（結核性腹水、結核瘤、皮膚結核等）證據不足；禽型結核病、蕁麻疹、肝片吸蟲症、肉毒中毒、尿素循環障礙等機轉上不合理，很可能是知識圖譜的假象。

**若要推進需要：**
- 取得 delamanid 對 *M. bovis* 的體外藥敏（MIC）或動物模型數據
- 補齊 DrugBank 作用機轉資料，以及香港衛生署仿單的警語與禁忌症
- 若轉向非活動性結核病：等待 PHOENIx 試驗結果。預防性使用前，需建立 QT 間期延長監測，並檢視低白蛋白血症與 CYP 交互作用
- 釐清「inactive tuberculosis」的定義（本報告暫解讀為潛伏結核感染或預防性治療）

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

