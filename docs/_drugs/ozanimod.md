---
layout: default
title: Ozanimod
parent: 中證據等級 (L3-L4)
nav_order: 642
evidence_level: L3
indication_count: 1
---

# Ozanimod
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

# Ozanimod：從復發型多發性硬化症到漸進復發型多發性硬化症

## 一句話總結

Ozanimod 是口服 S1P 受體調節劑，已核准用於復發型多發性硬化症（MS）。
TxGNN 模型預測它可能對**漸進復發型多發性硬化症 (Progressive Relapsing Multiple Sclerosis)** 有效。
目前有 **7 個臨床試驗**和 **20 篇文獻**，但沒有任何一項直接證實 ozanimod 對此型態的療效。這個預測與已核准的適應症高度重疊，不是典型的藥物再利用案例。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 復發型多發性硬化症（依文獻與美國 FDA 核准資訊；香港許可證未載明適應症文字） |
| 預測新適應症 | 漸進復發型多發性硬化症 (Progressive Relapsing Multiple Sclerosis) |
| TxGNN 預測分數 | 99.34% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Ozanimod 是選擇性 S1P1/S1P5 受體調節劑。它讓淋巴球滯留在淋巴結內，減少自體反應性淋巴球浸潤中樞神經系統，因此能控制由復發驅動的發炎性疾病活動。DrugBank 的作用機轉欄位目前缺漏，以上說明來自評估資料中的機轉推論。

「漸進復發型 MS」是舊的分型名稱，現在多半重新歸類為「伴有活動性的原發進展型 MS」。這個適應症與 ozanimod 已核准的復發型 MS 大幅重疊，所以 TxGNN 給出 0.993 的高分，很可能只是反映這種重疊。

至於對非發炎性進展（神經退化）是否有效，目前只有間接證據。最接近的來源是進展型 MS 的網絡統合分析（PMID 39254048），但它並未特別支持 ozanimod。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02576717](https://clinicaltrials.gov/study/NCT02576717) | Phase 3 | 完成 | 2494 | 隨機、雙盲、活性對照試驗，用於復發型 MS。摘要未直接顯示藥名（RPC1063 為 ozanimod 開發代號），建議核對。對漸進復發型屬間接證據 |
| [NCT06396039](https://clinicaltrials.gov/study/NCT06396039) | Phase 4 | 進行中（不再招募） | 84 | 中國成人復發型 MS 的單臂開放性療效與安全性研究，僅提供輔助性真實世界證據 |
| [NCT05605782](https://clinicaltrials.gov/study/NCT05605782) | N/A | 進行中（不再招募） | 9000 | ORION 上市後長期安全性觀察研究，有安全性資料，無進展型療效證據 |
| [NCT05828901](https://clinicaltrials.gov/study/NCT05828901) | N/A | 招募中 | 60 | 觀察 S1P 受體調節劑治療後的疾病活動與反彈風險，屬類別相關，規模小 |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | 進行中（不再招募） | 900 | 早期積極治療 vs 逐步升級治療的實用性策略試驗，非 ozanimod 專屬 |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | 進行中（不再招募） | 800 | DELIVER-MS：早期高效 DMT vs 逐步升級策略，非 ozanimod 專屬 |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | 邀請招募中 | 323 | STATURE：六種口服 DMT（含 ozanimod）的治療負擔與服藥依從性觀察，與進展型無關 |

另有 NCT05688436 為 diroximel fumarate 的懷孕結局登記，與 ozanimod 無關，不列入。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | 網絡統合分析 | Cochrane Database Syst Rev | 進展型 MS 的免疫調節與免疫抑制治療，各藥缺乏直接比較試驗，相對療效與安全性仍不明確 |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | 網絡統合分析 | Cochrane Database Syst Rev | 比較復發緩解型 MS 各類免疫調節與免疫抑制治療的相對效益 |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | Review | Neurology International | Ozanimod 治療復發型 MS 的疾病、療效與副作用綜述 |
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | Review | Drugs | Ozanimod 首次核准摘要：美國 FDA 於 2020 年 3 月核准用於復發型 MS，含臨床孤立症候群、復發緩解型與活動性次發進展型 |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | Review | Expert Opin Pharmacother | S1P 受體調節劑（含 ozanimod）用於復發型 MS 的最新進展 |
| [33797705](https://pubmed.ncbi.nlm.nih.gov/33797705/) | 2021 | Review | CNS Drugs | S1P 受體調節劑用於 MS 的整體回顧 |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | Review | Ther Adv Neurol Disord | 進展型 MS 的最新治療發展與未來方向 |
| [37638037](https://pubmed.ncbi.nlm.nih.gov/37638037/) | 2023 | 前臨床研究 | Front Immunol | S1PR-1/5 調節劑 RP-101074 在中樞神經退化模型中顯示有益效果，提供機轉面的間接支持 |
| [35805142](https://pubmed.ncbi.nlm.nih.gov/35805142/) | 2022 | Review | Cells | S1P 訊號路徑調節劑的現況與未來展望 |
| [30410033](https://pubmed.ncbi.nlm.nih.gov/30410033/) | 2018 | Review | Nat Rev Dis Primers | 多發性硬化症的整體疾病綜述 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67126 | ZEPOSIA CAPSULES 0.23MG AND 0.46MG (TREATMENT INITIATION PACK) | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD |
| HK-67127 | ZEPOSIA CAPSULES 0.92MG | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Ozanimod 在香港已上市，且已核准用於復發型 MS。有一個已完成的 Phase 3 RCT（NCT02576717），但屬復發型人群，對漸進復發型只是間接證據，所以證據等級定為 L3。
- 這個預測與已核准適應症大幅重疊，不是真正的新適應症，也沒有證據顯示它能改善與復發無關的失能進展。

**使用護欄：**
- 僅限臨床或影像學上有活動性疾病的患者。
- 不宣稱對與復發無關的失能進展有效。
- 依核准仿單持續監測心臟、肝臟、感染與黃斑部水腫。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症。
- 補齊 DrugBank 作用機轉資料。
- 確認 NCT02576717 與 NCT06396039 的藥物身分。
- 取得 ozanimod 在無活動性的進展型 MS 的直接臨床證據。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

