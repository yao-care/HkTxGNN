---
layout: default
title: Rimegepant
parent: 高證據等級 (L1-L2)
nav_order: 651
evidence_level: L2
indication_count: 5
---

# Rimegepant
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Rimegepant：從偏頭痛急性治療到腦幹型先兆偏頭痛

## 一句話總結

Rimegepant 是一種選擇性 CGRP（降鈣素基因相關胜肽）受體拮抗劑（gepant 類），已在美國/歐盟核准用於成人偏頭痛急性治療及陣發性偏頭痛預防性治療，但**尚未在香港上市**。
TxGNN 模型預測它可能對**腦幹型先兆偏頭痛 (Migraine with Brainstem Aura)** 特別有效，
目前**無直接針對此亞型設計的臨床試驗**，但有 **15 篇相關文獻**支持其藥理機轉合理性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 偏頭痛急性治療（伴或不伴先兆）及陣發性偏頭痛預防性治療（美國/歐盟已核准；香港未上市，非正式引用） |
| 預測新適應症 | 腦幹型先兆偏頭痛 (Migraine with Brainstem Aura) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏正式的 DrugBank 作用機轉 (MOA) 結構化資料。根據文獻，Rimegepant 是選擇性 CGRP 受體拮抗劑，透過阻斷偏頭痛神經血管發炎路徑中 CGRP 的作用而發揮療效，已核准用於偏頭痛急性與預防性治療。

與傳統 triptan 類藥物不同，gepants（包括 rimegepant）**不具血管收縮作用**。這一點在腦幹型先兆偏頭痛（舊稱 basilar-type migraine）病人族群中特別重要——triptan 類藥物因其血管收縮機轉，在此亞型病人中屬於相對禁忌或需謹慎使用，而 CGRP 拮抗劑理論上可避開此風險，因此臨床指引傾向優先考慮 gepants 類藥物於此亞型。

然而，現有的第三期／第四期臨床試驗（如 NCT 對應文獻 PMID 41066271、41366286）多以**一般偏頭痛族群**為收案對象，尚未見到針對「brainstem aura」亞型專門設計的隨機對照試驗。因此本預測的證據基礎屬於「藥理機轉延伸＋一般偏頭痛族群療效外推」，而非亞型特異性直接證據，這也是 TxGNN 評分雖高但證據等級僅列為 L2 的原因。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | 網絡統合分析（基於 RCT） | J Headache Pain | 比較 lasmiditan、rimegepant、ubrogepant 三種新型急性偏頭痛藥物之相對療效 |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Phase 3 開放性長期安全性研究 | Cephalalgia | 中國成人偏頭痛病人使用 rimegepant 75mg ODT 的長期安全性與有效性評估 |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Phase 4 開放性安全性研究 | J Headache Pain | 每日一次 rimegepant 75mg 用於陣發性偏頭痛預防之 24 週安全性與耐受性 |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Review | CNS Drugs | 綜述 rimegepant 於偏頭痛急性與預防治療之療效，Phase 3 試驗顯示優於安慰劑 |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Review（核准摘要） | Drugs | Rimegepant 首次核准摘要，說明其為高選擇性 CGRP 拮抗劑 |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review（gepant 類） | Handbook Clin Neurol | 回顧 CGRP 受體拮抗劑（gepants）之發展史，含血管安全性優勢說明 |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | Pain Management | 回顧三種新型急性偏頭痛治療選項（含 rimegepant），聚焦神經血管機轉 |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | 回溯性世代分析 | Headache | 評估 rimegepant 於青少年偏頭痛病人（仿單外使用）之耐受性與有效性 |
| [41574090](https://pubmed.ncbi.nlm.nih.gov/41574090/) | 2026 | 縱貫性 MRA 影像研究 | Brain Communications | 探討 rimegepant 對偏頭痛發作時腦內外動脈之直接血管效應（非血管收縮機轉證據） |
| [32993366](https://pubmed.ncbi.nlm.nih.gov/32993366/) | 2021 | Review | Ann Pharmacother | 回顧 CGRP 受體拮抗劑與 5-HT1F 促效劑之療效、安全性與成本比較 |

---

## 香港上市資訊

目前未在香港取得藥品許可證，無核准適應症資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本評估資料庫尚未取得 TFDA 仿單警語、禁忌症及藥物交互作用資料，為 Blocking 等級資料缺口。）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Rimegepant 不具血管收縮機轉，在藥理學上合理適用於腦幹型先兆偏頭痛此一 triptan 類藥物相對禁忌的亞群；且有 1 篇基於 RCT 的網絡統合分析及多篇 Phase 3/4 一般偏頭痛族群試驗支持整體療效與安全性，但**缺乏亞型特異性直接證據**。（其餘 4 個 TxGNN 高分候選適應症因無任何機轉關聯或文獻支持，已判定為知識圖譜雜訊，予以 Hold。）

**若要推進需要：**
- 取得仿單警語、禁忌症與藥物交互作用資料（現為 Blocking 缺口，無法進入安全性初評）
- 補齊正式作用機轉 (MOA) 結構化資料
- 針對腦幹型先兆偏頭痛亞型的專門臨床試驗或真實世界資料
- 評估香港上市申請可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

