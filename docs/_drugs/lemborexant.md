---
layout: default
title: Lemborexant
parent: 僅模型預測 (L5)
nav_order: 508
evidence_level: L5
indication_count: 1
---

# Lemborexant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Lemborexant：從失眠治療到入睡與維持睡眠障礙（既有用途的模型驗證）

## 一句話總結

Lemborexant（香港商品名 DAYVIGO）是雙重食慾素受體拮抗劑，文獻顯示它已在美國、日本、加拿大核准用於成人失眠。
TxGNN 預測它可能對**入睡與維持睡眠障礙 (sleep disorder, initiating and maintaining sleep)** 有效，但這與它既有的適應症一致，屬於對已知用途的確認，並非真正的新適應症。
目前有 **1 個臨床試驗登記**和 **20 篇文獻**，其中包含多篇 Phase 3 RCT。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 入睡與維持睡眠障礙 (sleep disorder, initiating and maintaining sleep) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L1（依據已發表的 Phase 3 RCT 文獻；登記的試驗僅有 1 個未開始招募的 Phase 2） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Lemborexant 資料庫中的作用機轉欄位缺漏，以下說明來自文獻（如 PMID 35972717、37086045），不是本次輸入資料。它是雙重食慾素受體 (OX1R/OX2R) 拮抗劑，透過阻斷促進清醒的食慾素訊號，縮短入睡時間並減少入睡後的清醒時間。

預測的疾病是入睡與維持睡眠障礙，也就是失眠，與藥物機轉直接對應。TxGNN 給出的高分（99.75%）與這個機轉一致。

需要注意的是，失眠本來就是 Lemborexant 的已上市適應症。本次輸入資料中原適應症欄位為空，因此這個結果只能視為對既有用途的確認，不代表發現新的適應症。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06928766](https://clinicaltrials.gov/study/NCT06928766) | Phase 2 | 尚未招募 | 15 | 比較 eszopiclone 與 lemborexant 用於低覺醒閾值的阻塞性睡眠呼吸中止症 (OSA) 合併難以入睡或維持睡眠的患者；雙盲、安慰劑對照，尚無結果 |

此試驗針對合併 OSA 的次族群，並非原發性失眠，因此不增加療效證據，但與呼吸相關風險的評估有關。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | 在老年失眠患者中，比較 lemborexant、安慰劑與 zolpidem 緩釋劑 |
| [32585700](https://pubmed.ncbi.nlm.nih.gov/32585700/) | 2020 | RCT (Phase 3) | Sleep | SUNRISE 2：評估 lemborexant 相較安慰劑在成人失眠的長期療效與耐受性 |
| [33636648](https://pubmed.ncbi.nlm.nih.gov/33636648/) | 2021 | RCT (Phase 3) | Sleep Med | SUNRISE-2：最長 12 個月連續使用 lemborexant 的療效與安全性 |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | 系統性回顧/網絡統合分析 | Lancet | 比較各類藥物對成人失眠的急性與長期治療效果 |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | 系統性回顧/網絡統合分析 | Transl Psychiatry | 比較 daridorexant、lemborexant、suvorexant 三種 DORA 的療效與安全性 |
| [36701954](https://pubmed.ncbi.nlm.nih.gov/36701954/) | 2023 | 系統性回顧/網絡統合分析 | Sleep Med Rev | 比較 20 種藥物治療成人失眠的療效與耐受性 |
| [32531478](https://pubmed.ncbi.nlm.nih.gov/32531478/) | 2020 | 系統性回顧/網絡統合分析 | J Psychiatr Res | lemborexant 與 suvorexant 的療效與安全性比較 |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | 網絡統合分析 | J Manag Care Spec Pharm | lemborexant 與其他失眠治療的療效比較 |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | 事後分析 | Sleep Med | lemborexant 對失眠合併輕度 OSA 患者睡眠結構的影響 |
| [32096020](https://pubmed.ncbi.nlm.nih.gov/32096020/) | 2020 | 藥物綜述 | Drugs | Lemborexant 首次核准：美國於 2019 年 12 月核准用於成人失眠 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-67002 | DAYVIGO TABLETS 5MG | EISAI (HONG KONG) COMPANY LIMITED |
| HK-67001 | DAYVIGO TABLETS 10MG | EISAI (HONG KONG) COMPANY LIMITED |

輸入資料未提供劑型與核准適應症文字。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多篇已發表的 Phase 3 RCT 與網絡統合分析支持 Lemborexant 用於失眠，證據等級為 L1，且香港已有 2 張上市許可證。
- 這個預測是對既有適應症的確認，不是新用途。安全性資料（仿單警語、禁忌症）仍缺漏，因此需設下防護條件。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認核准適應症、警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 若考慮合併 OSA 的族群，追蹤 NCT06928766 的結果，並評估呼吸方面的安全性

本報告僅供研究參考，不構成醫療建議，任何臨床應用均需經過臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

