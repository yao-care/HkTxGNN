---
layout: default
title: Zolpidem
parent: 僅模型預測 (L5)
nav_order: 945
evidence_level: L5
indication_count: 3
---

# Zolpidem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Zolpidem：從失眠症（許可證資料未載明）到入睡與維持睡眠障礙

## 一句話總結

Zolpidem 是非苯二氮平類（Z-drug）安眠藥，臨床上用於失眠治療。
TxGNN 預測它可能對**入睡與維持睡眠障礙 (sleep disorder, initiating and maintaining sleep)** 有效，
目前**無臨床試驗登記**，但有 **18 篇文獻**，其中包含隨機對照試驗與網絡統合分析。
這其實不是真正的老藥新用，失眠本來就是 Zolpidem 的既有適應症，只是來源資料沒有填寫原適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明（臨床上為失眠） |
| 預測新適應症 | 入睡與維持睡眠障礙 (sleep disorder, initiating and maintaining sleep) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L3（依判定規則：有系統性回顧與網絡統合分析，但無已完成的 Phase 3 試驗登記；Evidence Pack 自帶標示為 L1） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Zolpidem 是 GABA-A 受體的正向異位調節劑，對 α1 亞基有選擇性。
它產生鎮靜與安眠作用，能縮短入睡時間並幫助維持睡眠。
這與模型給出的高分（0.9987）一致。

這個預測的合理性來自藥物本身的既有用途。文獻（如 Greenblatt 2012、Monti 2017）都把 Zolpidem 描述為廣泛使用的失眠藥物。
原適應症欄位為空、作用機轉標示為缺漏，是來源資料不完整，不代表沒有核准用途。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | Lemborexant 對照安慰劑與 Zolpidem 緩釋劑，用於老年失眠患者 |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Intern Med | 以遮蔽減量加行為介入，協助停用苯二氮平受體促效劑（含 Z-drugs）類安眠藥 |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | RCT（事後分析） | Sleep Med | Lemborexant 對失眠合併輕度阻塞性睡眠呼吸中止患者睡眠結構的影響（非針對 Zolpidem） |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | 系統性回顧／網絡統合分析 | Lancet | 比較成人失眠急性與長期藥物治療的相對效果 |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | 系統性回顧／網絡統合分析 | J Manag Care Spec Pharm | 比較 Lemborexant 與其他失眠治療的療效與安全性 |
| [41101148](https://pubmed.ncbi.nlm.nih.gov/41101148/) | 2025 | 網絡統合分析／FAERS 分析 | Sleep Med | 以貝氏網絡統合與通報資料，比較 DORA、苯二氮平類、Z-drugs 等失眠藥物的療效與安全性 |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Z-drugs 有證據支持，但有認知損害、耐受性、停藥反彈性失眠、跌倒與依賴等副作用 |
| [28262178](https://pubmed.ncbi.nlm.nih.gov/28262178/) | 2017 | Review | Asian J Psychiatry | Zolpidem 為短效咪唑吡啶類安眠藥，另有緩釋、舌下錠與口腔噴劑等新劑型 |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Review | Expert Opin Pharmacother | Zolpidem 作用於苯二氮平受體，是美國處方量最大的安眠藥 |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Review | J Fam Pract | 失眠在基層醫療中常被忽略，應視為獨立疾病治療 |

---

## 香港上市資訊

香港共有 19 張許可證，以下列出 5 張。來源資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62293 | ZOPIM FILM COATED TABLETS 10MG | PHARMASON COMPANY LIMITED |
| HK-55031 | VICKNOX-B TAB 10MG | JEAN-MARIE PHARMACAL CO LTD |
| HK-64074 | EURO-ZOLPIDEM TABLETS 10MG | VICKMANS LABORATORIES LTD |
| HK-68646 | ZOLPIDEM HBPHARMA TABLETS 10MG | HIGHBURY PHARMA (HK) LIMITED |
| HK-54140 | ZOLMAN F.C. TAB 10MG | STAR MEDICAL SUPPLIES LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。
香港衛生署仿單的警語與禁忌尚未取得，這是目前的阻斷性資料缺口。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 失眠是 Zolpidem 的既有適應症，香港已有 19 張許可證，文獻也有多項 RCT 與網絡統合分析。
- 但沒有臨床試驗登記，仿單安全性資料也尚未取得。
- 使用上需注意：美國仿單對複雜睡眠行為有加框警語，且僅限短期治療。同時要留意依賴性、隔日功能受損，以及老年人跌倒風險。

**若要推進需要：**
- 下載並解析香港衛生署仿單，補齊警語與禁忌症。
- 從 DrugBank 補上作用機轉資料。
- 補上許可證的核准適應症與劑型欄位，修正原適應症為空的問題。

**其他預測（皆建議 Hold）：**
- **嬰兒良性陣發性斜頸**（分數 99.26%）：沒有明確機轉關聯，Zolpidem 也不適用於嬰兒，應視為知識圖譜的假象。
- **懼曠症**（分數 99.25%）：機轉關聯屬推測，Zolpidem 的抗焦慮作用弱，也無試驗或文獻。一線治療已有 SSRI/SNRI 與認知行為治療，且 GABA-A 類安眠藥的依賴風險在焦慮族群中更需顧慮。

---

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

