---
layout: default
title: Betahistine
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Betahistine：預測新適應症為周邊性眩暈 (Peripheral Vertigo)（證據等級 L5）。原適應症：梅尼爾氏症（Meniere disease）、內淋巴水腫（endolymphatic hydrops）"
monitor_inn: "Betahistine"
predicted_indications: ["restless legs syndrome", "otosclerosis", "peripheral vertigo", "age-related hearing impairment", "vertigo, benign recurrent, 2", "autosomal recessive hyperinsulinism due to Kir6.2 deficiency", "hyperinsulinemic hypoglycemia, familial"]
---

# Betahistine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Betahistine：從梅尼爾氏症到周邊性眩暈

## 一句話總結

Betahistine 是組織胺類似物，原本用於梅尼爾氏症（Meniere disease）與內淋巴水腫的治療。
TxGNN 模型預測的新適應症中，證據最完整的是**周邊性眩暈 (Peripheral Vertigo)**，目前有 **1 項已發表 RCT（BEMED）**、**2 篇 Cochrane 系統性回顧**與多篇文獻；但這大致仍屬於已核准的梅尼爾氏症／眩暈用途，並非真正的跨領域再利用，且已發表的療效證據並不一致。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 梅尼爾氏症（Meniere disease）、內淋巴水腫（endolymphatic hydrops） |
| 預測新適應症 | 周邊性眩暈 (Peripheral Vertigo) |
| TxGNN 預測分數 | 98.07% |
| 證據等級 | L1（依已發表 RCT 與 Cochrane 回顧判定；無登記臨床試驗） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Betahistine 是組織胺 H1 受體的弱促效劑，同時是 H3 受體的強效拮抗劑／反向促效劑。目前認為它透過改善內耳微循環（如增加耳蝸血流），並透過組織胺調節促進中樞前庭代償，進而緩解眩暈。

梅尼爾氏症本身就是周邊前庭疾病的一種，因此預測對周邊性眩暈有效，機轉上相當合理。Betahistine 已在多國用於梅尼爾氏症、良性陣發性姿勢性眩暈（BPPV）、前庭神經炎等周邊性眩暈。

需要說明的是，這個預測**大致屬於既有適應症的延伸**，不是真正的新領域再利用。此外，BEMED 試驗與 Cochrane 回顧顯示相較於安慰劑的獲益有限或不一致，療效宣稱應保持審慎。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26797774](https://pubmed.ncbi.nlm.nih.gov/26797774/) | 2016 | RCT | BMJ | BEMED 試驗：長期、多中心、雙盲、安慰劑對照、劑量探討試驗；後續評論指出 betahistine 在減少眩暈發作次數上未顯著優於安慰劑 |
| [36827524](https://pubmed.ncbi.nlm.nih.gov/36827524/) | 2023 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | 評估 betahistine、利尿劑、抗病毒藥與類固醇等全身性藥物對梅尼爾氏症的效果 |
| [27327415](https://pubmed.ncbi.nlm.nih.gov/27327415/) | 2016 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | 評估 betahistine 相較安慰劑對各種原因眩暈症狀的效果 |
| [23778722](https://pubmed.ncbi.nlm.nih.gov/23778722/) | 2014 | 統合分析 | Eur Arch Otorhinolaryngol | 12 項雙盲、隨機、安慰劑對照研究，探討 betahistine 對梅尼爾氏症與前庭性眩暈的反應 |
| [12582782](https://pubmed.ncbi.nlm.nih.gov/12582782/) | 2003 | RCT | Eur Arch Otorhinolaryngol | 144 位梅尼爾氏症或陣發性姿勢性眩暈患者，雙盲安慰劑對照比較 betahistine 的療效與安全性 |
| [41487075](https://pubmed.ncbi.nlm.nih.gov/41487075/) | 2026 | RCT | J Otolaryngol Head Neck Surg | 比較銀杏萃取物 EGb 761 與 betahistine 用於病因不明的頭暈／眩暈 |
| [26245698](https://pubmed.ncbi.nlm.nih.gov/26245698/) | 2015 | Review | Acta Otolaryngol | 臨床研究與統合分析顯示 betahistine 對梅尼爾氏症、BPPV、前庭神經炎等周邊性眩暈有效且安全 |
| [41038567](https://pubmed.ncbi.nlm.nih.gov/41038567/) | 2025 | 系統性回顧 | Acta Otorrinolaringol Esp | 比較 cinnarizine/dimenhydrinate 複方與 betahistine 治療眩暈的療效與安全性 |
| [37000080](https://pubmed.ncbi.nlm.nih.gov/37000080/) | 2023 | 系統性回顧與統合分析 | Medicine | 評估 Epley 手法加 betahistine 用於後半規管 BPPV |
| [24177346](https://pubmed.ncbi.nlm.nih.gov/24177346/) | 2013 | 評論 | J Vestib Res | 闡明 betahistine 緩解眩暈與促進前庭代償的作用機轉 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37181 | BETASERC TAB 8MG | 錠劑 | 未提供 |
| HK-38792 | BETASERC TAB 16MG | 錠劑 | 未提供 |
| HK-51514 | BETASERC TAB 24MG | 錠劑 | 未提供 |
| HK-49502 | BETA-SYNTO TAB 8MG | 錠劑 | 未提供 |
| HK-45998 | ALFINOR 8 TAB 8MG | 錠劑 | 未提供 |

共 11 張有效單方許可證，上表僅列出其中 5 張；其餘為 METERLON、UNDIZZ、EFORMAT、BETAHIST FORTE、JOYISH 等品牌。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 周邊性眩暈有已發表 RCT（BEMED）、Cochrane 回顧與統合分析支持，且 betahistine 已在香港上市，機轉合理。但這屬於既有用途的延伸，且 BEMED 與 Cochrane 顯示相較安慰劑的獲益有限或不一致，因此需審慎宣稱療效。

**若要推進需要：**
- 取得香港衛生署核准仿單，確認核准適應症、警語與禁忌症
- 取得詳細的作用機轉資料（MOA）
- 針對 BEMED 與 Cochrane 的不一致結果做進一步證據整合，並界定可能受益的亞群（如特定病因或劑量）
- 若要在周邊性眩暈中主張特定適應症，需補充登記的臨床試驗證據

**其他預測適應症備註：**
- 活動期梅尼爾氏症（前庭型）：L3，Proceed with Guardrails；為梅尼爾氏症亞型，證據以回顧與觀察性研究為主。
- 活動期梅尼爾氏症（耳蝸型）：L4，Hold；僅有機轉與前臨床研究（耳蝸血流）。
- 活動期梅尼爾氏症（耳蝸前庭型）：L4，Hold；無專屬證據，僅為間接支持。
- 良性復發性眩暈 2 型：L2，列為研究問題；證據多來自鄰近的 BPPV 研究。
- 耳硬化症：L4，Hold；證據間接，至多緩解伴隨的前庭症狀。
- 不寧腿症候群、老年性聽力損失：L5，Hold；僅有模型預測。
- 高胰島素血症相關疾病（Kir6.2 缺乏、家族性高胰島素低血糖）：L5，Hold；無合理機轉連結，可能為知識圖譜的假關聯。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

