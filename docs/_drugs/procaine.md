---
layout: default
title: Procaine
parent: 中證據等級 (L3-L4)
nav_order: 718
evidence_level: L4
indication_count: 10
---

# Procaine
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

# Procaine：從局部麻醉到高鐵血紅素血症（反向安全訊號）

## 一句話總結

Procaine 是芳香胺類局部麻醉藥，香港登記的產品為心臟停搏液灌注用無菌濃縮液。
TxGNN 預測它可能對**高鐵血紅素血症 (Methemoglobinemia)** 有效，但文獻顯示方向相反：procaine 是**誘發**此病的原因，不是治療藥。
目前**沒有臨床試驗**，只有 **8 篇文獻**（多為個案報告），建議把這個預測視為安全警訊，不當作治療假說。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症（登記品項為心臟停搏液灌注用無菌濃縮液） |
| 預測新適應症 | 高鐵血紅素血症 (Methemoglobinemia) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Procaine 屬於芳香胺類局部麻醉藥，也是鈉通道阻斷劑，但現有資料無法建立它與高鐵血紅素血症之間的治療性機轉。

這個預測的合理性很低。TxGNN 分數雖高（99.50%），文獻卻顯示 procaine（及其他芳香胺類麻醉藥，如 lignocaine）會導致高鐵血紅素血症。模型的關聯很可能來自知識圖譜中的「藥物－不良反應」連結，而不是治療關係。

排名第 2 的「methemoglobinemia, alpha type」和排名第 5 的「methemoglobin reductase deficiency」也是同一類訊號。它們沒有任何試驗或文獻，很可能是共享圖譜鄰居所致。後者的患者尤其容易受誘發高鐵血紅素的藥物影響，因此也應視為安全顧慮。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | 臨床研究 | Zhonghua Wai Ke Za Zhi | 探討靜脈注射 procaine 麻醉對高鐵血紅素濃度的影響（無摘要，依標題判斷） |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Review | Laval Medical | 局部麻醉藥綜述 |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | 局部麻醉藥的合理使用：需了解藥理特性、技術與病人臨床狀態 |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Review | Fundam Appl Toxicol | 有機磷殺蟲劑的毒性交互作用機轉，與本適應症僅間接相關 |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | 個案報告 | Lancet | 使用 lignocaine 後發生高鐵血紅素血症 |
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | 個案報告 | Acta Physiol Latino Am | 靜脈注射 procaine 引起高鐵血紅素血症 |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | 個案報告 | Rev Esp Anestesiol Reanim | 新生兒全身麻醉中皮下浸潤 novocaine（procaine）後發生高鐵血紅素血症 |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | 藥動學研究 | Am J Obstet Gynecol | Procaine 與對胺基苯甲酸可通過人類胎盤 |

文獻均為舊資料，且多數指向 procaine 導致高鐵血紅素血症，沒有支持治療用途的證據。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66905 | STERILE CONCENTRATE FOR CARDIOPLEGIA INFUSION | 未載明 | 未載明 |

製造商為 THE INTERNATIONAL MEDICAL COMPANY LIMITED。

## 安全性考量

安全性資訊請參考原廠仿單。目前未取得香港衛生署仿單的警語與禁忌資料，藥物交互作用查詢也沒有結果。

文獻中有兩項值得注意的安全訊號，並非仿單內容：
- **高鐵血紅素血症**：多篇個案報告顯示 procaine 與其他芳香胺類麻醉藥可誘發，新生兒也有案例。
- **類過敏／過敏反應**：排名第 4 的「anaphylaxis」文獻多為 procaine 或 procaine-penicillin 引發的類過敏反應（如 Hoigné 症候群），屬不良事件報告。

## 結論與下一步

**決策：Hold**

**理由：**
- 高分預測與文獻方向相反，證據顯示 procaine 是高鐵血紅素血症的誘因，沒有任何臨床試驗，無法支持治療性再利用。
- 安全性仿單資料與作用機轉資料都缺漏，無法進入安全性篩選。

**其他候選方向（僅為研究問題，非推薦）：**
- **纖維肌痛症 (fibromyalgia)**，TxGNN 99.23%：有 5 篇 1951–1970 年的 procaine 注射治療「纖維組織炎」與顏面痛報告，機轉上合理（局部麻醉／鈉通道阻斷），但皆為低層級舊資料，且「fibrositis」不等同現代診斷標準。
- **肌腱炎 (tendinitis)**，TxGNN 99.20%：2022 年有一項關於神經療法（常用 procaine）治療棘上肌肌腱病變的研究（PMID 35480510），但使用藥物與研究設計尚無法從標題確認，需讀全文再評估。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料。
- 補齊作用機轉資料（例如查詢 DrugBank）。
- 針對高鐵血紅素血症，改以藥物安全訊號處理，不作為治療候選。
- 若要探討纖維肌痛症或肌腱炎，先閱讀 PMID 35480510 全文，並規劃現代對照研究。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

