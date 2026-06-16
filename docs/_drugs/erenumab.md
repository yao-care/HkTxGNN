---
layout: default
title: Erenumab
parent: 中證據等級 (L3-L4)
nav_order: 277
evidence_level: L3
indication_count: 1
---

# Erenumab
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

# Erenumab：從偏頭痛到腦幹先兆偏頭痛

## 一句話總結

Erenumab 是靶向 CGRP 受體的全人類化單株抗體，在國際上核准用於發作性及慢性偏頭痛的預防治療。
TxGNN 模型預測它可能對**腦幹先兆偏頭痛 (Migraine with Brainstem Aura)** 有效，
目前有 **0 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 偏頭痛預防（發作性及慢性，國際核准） |
| 預測新適應症 | 腦幹先兆偏頭痛 (Migraine with Brainstem Aura) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Erenumab 靶向 CGRP 受體（CLR/RAMP1 複合體），透過阻斷降鈣素基因相關胜肽（CGRP）的訊號傳遞來預防偏頭痛發作。CGRP 是三叉血管系統（trigeminovascular system）發炎與疼痛傳導的核心信號分子，在偏頭痛發作期間大量釋放，驅動顱內血管擴張與硬腦膜神經源性發炎。

腦幹先兆偏頭痛（前稱「基底型偏頭痛」，ICHD-3 修訂分類）的病理生理涉及腦幹核（locus coeruleus、PAG 等）的異常激活，以及三叉血管迴路的廣泛參與，CGRP 正是此過程的關鍵調節因子。與 triptan 及麥角鹼不同，erenumab 不誘導直接血管收縮，理論上規避了傳統療法在基底動脈供血區可能引發缺血的安全疑慮，在腦幹先兆偏頭痛中具潛在的安全性優勢。

TxGNN 知識圖譜預測分數高達 99.89%，反映 CGRP 受體節點與腦幹先兆偏頭痛疾病節點在知識圖譜中的強關聯，與上述機轉理論高度吻合。值得注意的是，目前 erenumab 在有先兆偏頭痛族群中已有多項臨床研究支持，為類推至腦幹先兆亞型提供了間接依據。

---

## 臨床試驗證據

目前無針對腦幹先兆偏頭痛（Migraine with Brainstem Aura）的相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic Review | Int Immunopharmacol | Erenumab 在發作性與慢性偏頭痛預防的系統性回顧，確認療效與安全性 |
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | Phase 3 RCT | Lancet | LIBERTY 試驗：2-4 種前線預防治療失敗的發作性偏頭痛患者中，erenumab 50/140 mg 均顯示顯著療效 |
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | Post-hoc RCT 亞組分析 | JAMA Neurology | 有先兆與無先兆偏頭痛亞組分析：erenumab 在兩亞組均有效，有先兆患者無額外血管安全疑慮 |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | 前瞻性安全性分析 | Headache | 長期臨床試驗 pooled data：不同心血管風險程度患者（含先兆偏頭痛）使用 erenumab 均未見顯著心血管事件增加 |
| [40275185](https://pubmed.ncbi.nlm.nih.gov/40275185/) | 2025 | 前瞻性生物標記子研究 | J Headache Pain | REFORM 試驗子研究：先兆偏頭痛患者血漿 suPAR（全身發炎標記）升高，與 CGRP 靶向療法反應具關聯性 |
| [32867533](https://pubmed.ncbi.nlm.nih.gov/32867533/) | 2021 | 機轉/交叉研究 | Cephalalgia | Erenumab 不影響腦血管舒縮反應與血流介導舒張，支持在腦幹先兆偏頭痛中使用的血管安全性 |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | 真實世界世代（回顧性）| Clin Neurol Neurosurg | 克羅埃西亞真實世界研究：多種預防治療失敗的慢性偏頭痛，6 個月 erenumab 療效與耐受性良好 |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | 深入闡述 CGRP 在偏頭痛（含先兆亞型）的三叉血管系統角色，為 CGRP 靶向療法提供機轉基礎 |
| [35538414](https://pubmed.ncbi.nlm.nih.gov/35538414/) | 2022 | 真實世界研究 | J Headache Pain | 12 個月真實世界安全性研究：erenumab 整體耐受性良好，不良事件具時間依賴性，可預測管理 |
| [33998825](https://pubmed.ncbi.nlm.nih.gov/33998825/) | 2021 | 真實世界比較效益研究 | J Manag Care Spec Pharm | 美國真實世界研究：erenumab 有效降低急性止痛藥使用頻次及醫療資源消耗 |

---

## 香港上市資訊

Erenumab 目前在香港無已登記的藥物許可證，尚未上市。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
文獻中有系統性回顧與多項 Phase 3 RCT 支持 erenumab 在有先兆偏頭痛族群的療效及安全性（L3 等級），CGRP 受體阻斷與腦幹先兆偏頭痛病理機轉高度吻合，且相較傳統療法具潛在血管安全優勢；然而目前缺乏針對「腦幹先兆偏頭痛」此特定亞型的專屬臨床試驗，香港亦尚無上市許可。

**若要推進需要：**
- 取得原廠完整仿單，補充正式 MOA 說明、警語及禁忌症資料（現為資料缺口）
- 設計前瞻性研究，納入 ICHD-3 確診的腦幹先兆偏頭痛患者，評估 erenumab 療效
- 評估香港恩慈用藥（Compassionate Use）或擴大適應症申請途徑的可行性
- 治療期間監測基底動脈供血區的神經學症狀及血管影像學指標
- 確認個別患者的心血管風險分層，特別是有高風險因素的腦幹先兆偏頭痛患者
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

