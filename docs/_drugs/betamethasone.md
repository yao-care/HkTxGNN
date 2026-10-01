---
layout: default
title: Betamethasone
parent: 高證據等級 (L1-L2)
nav_order: 112
evidence_level: L2
indication_count: 10
---

# Betamethasone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Betamethasone：從外用皮質類固醇到圓形禿（Alopecia Areata）

## 一句話總結

Betamethasone 是強效糖皮質素（皮質類固醇），在香港以乳膏、頭皮外用製劑等形式上市。
TxGNN 模型預測它可能對**圓形禿 (Alopecia Areata)** 有效，
目前有 **7 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含多項隨機對照試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 圓形禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，資料庫未提供原適應症與 MOA。以下機轉推論來自藥物類別，而非資料庫紀錄。

Betamethasone 是強效糖皮質素，具有明確的抗發炎與免疫抑制作用。圓形禿是一種自體免疫疾病：毛囊的免疫豁免崩解後，T 細胞會攻擊毛囊，造成非疤痕性掉髮。糖皮質素能抑制這類 T 細胞介導的免疫攻擊，因此機轉上合理。

在臨床上，外用、病灶內注射與口服小劑量脈衝（mini-pulse）類固醇都是圓形禿的既有治療方式。多項研究把 betamethasone 當作治療組或對照組，與 latanoprost、minoxidil、cyclosporine、methotrexate、azathioprine 等藥物比較。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | 完成 | 60 | 比較每週 azathioprine 脈衝與口服 betamethasone 小劑量脈衝（BOMP）治療中重度圓形禿，直接評估 betamethasone |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | 完成 | 50 | 隨機比較外用 latanoprost 與外用 betamethasone 治療局部圓形禿的療效與安全性 |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | 不適用 | 未知 | 59 | 外用 cetirizine 1% 與 betamethasone valerate 0.1% 治療局部圓形禿，betamethasone 為對照 |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | 未知 | 60 | 外用 pentoxifylline 或 metformin 凝膠與 betamethasone valerate 0.1% 乳膏比較，早期試驗，推論有限 |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | 完成 | 40 | 外用 minoxidil 加強效外用類固醇，對比病灶內 triamcinolone 注射，未確認類固醇是否為 betamethasone |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | 未知 | 30 | Clobetasol 泡沫治療中央離心性疤痕性禿髮，藥物與疾病皆不同，關聯性低 |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | 招募中 | 250 | 中央離心性疤痕性禿髮多中心前瞻研究，未顯示涉及 betamethasone，關聯性低 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | J Am Acad Dermatol | 以微針經皮遞送複方 betamethasone 治療圓形禿，目的是改善病灶內注射的疼痛問題 |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | RCT | Cureus | 非盲、平行組隨機試驗（60 人），比較口服 cyclosporine 與 betamethasone 小劑量脈衝的療效與安全性 |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | RCT | Dermatol Ther | 雙盲六組隨機試驗，比較 latanoprost、minoxidil、betamethasone 及其組合 |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | RCT | J Dermatolog Treat | 受試者內隨機對照，比較病灶內 betamethasone 與 triamcinolone acetonide 治療局部圓形禿 |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT（依標題，資料庫分類為回溯比較） | Iran J Pharm Res | 36 名重度圓形禿患者，比較口服 betamethasone 每週脈衝、methotrexate 及兩者合併對比安慰劑 |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | 網絡統合分析 | Cochrane Database Syst Rev | 比較圓形禿的多種治療（免疫抑制劑、促毛髮生長劑、接觸免疫療法） |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | 回顧 | Dermatol Pract Concept | 回顧皮質類固醇脈衝療法治療圓形禿的療效、復發率、副作用與預後因子 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | 回顧 | Pediatr Dermatol | 回顧兒童圓形禿脈衝類固醇的劑量方案與副作用 |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | 臨床研究 | Cureus | 評估口服 betamethasone 小劑量脈衝治療中重度圓形禿的療效與安全性 |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | 比較性臨床研究 | Cureus | 比較外用 betamethasone dipropionate 與外用 minoxidil 治療圓形禿 |

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。資料庫未收錄其劑型與核准適應症文字，請以衛生署登記資料為準。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-45913 | AXCEL BETAMETHASONE CREAM 0.1% | KOTRA PHARMA (HONG KONG) COMPANY |
| HK-57560 | CIPROSONE CREAM 0.05% | ZENFIELDS (H.K.) LIMITED |
| HK-06910 | BETNOVATE SCALP APPLICATION 0.1% | GLAXOSMITHKLINE LIMITED |
| HK-28270 | SYNMETHASONE CREAM 0.1% | MARCHING PHARMACEUTICAL LIMITED |
| HK-27899 | BETCORTDERM CREAM 0.1% | EUROPHARM LAB CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個完成的 Phase 2 試驗（NCT06786689）直接評估口服 betamethasone 小劑量脈衝，另有多項 RCT 與一篇 Cochrane 網絡統合分析，證據等級為 L2。
- 資料中沒有 Phase 3 RCT，且多數試驗的樣本數小（30–60 人），betamethasone 常是對照組而非主要受試藥，因此不宜直接升級。
- 香港衛生署仿單的警語與禁忌尚未取得，安全性篩檢無法完成。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與交互作用。
- 補齊 MOA 與原適應症資料（可查 DrugBank）。
- 確認研究採用的給藥途徑（外用、病灶內、口服脈衝），與香港已上市劑型是否相符，再決定推進哪一種。
- 逐項核對各試驗的實際結果與療效指標，特別是 NCT06786689 與各 RCT，並釐清 betamethasone 究竟是治療組還是對照組。
- 設定長期或全身性類固醇使用的安全性監測計畫。

**其他預測適應症：**
- 網狀紅斑性黏蛋白沉積症（alopecia mucinosa）僅有老舊病例報告，為研究性問題。
- 休止期落髮、毛囊炎性禿髮等其餘預測缺乏 betamethasone 的直接證據或機轉依據，建議暫緩（Hold）。
- 特發性類固醇敏感型腎病症候群僅有 1981 年的單一報告，屬研究性問題。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

