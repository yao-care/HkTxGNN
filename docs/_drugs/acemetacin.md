---
layout: default
title: Acemetacin
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 1
---

# Acemetacin
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

# Acemetacin：從消炎止痛到骨關節炎易感性

## 一句話總結

Acemetacin 是 Indomethacin 的甘醇酸酯前驅藥（prodrug），在體內水解後釋放具活性的 Indomethacin，屬於非選擇性 COX 抑制劑類消炎止痛藥。
TxGNN 模型預測它可能對**骨關節炎易感性 (Osteoarthritis Susceptibility)** 有效，
但目前**尚無任何臨床試驗或文獻支持**，屬於純模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 消炎止痛（Indomethacin 前驅藥，NSAID 類） |
| 預測新適應症 | 骨關節炎易感性 (Osteoarthritis Susceptibility) |
| TxGNN 預測分數 | 99.22% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Acemetacin 是 Indomethacin 的甘醇酸酯（glycolic acid ester）前驅藥。進入體內後，經酯酶水解釋放出 Indomethacin（活性代謝物）。Indomethacin 是強效非選擇性 COX-1/COX-2 抑制劑，可阻斷花生四烯酸（arachidonic acid）轉化為前列腺素（尤其是 PGE₂）的路徑。

骨關節炎（OA）的核心病理機轉涵蓋滑膜炎症、軟骨基質破壞與關節疼痛，均與 COX 介導的前列腺素過度產生密切相關。Indomethacin 透過抑制 COX-1/COX-2，可直接干預上述病理機轉，理論上對 OA 的炎症反應與疼痛管理高度吻合。

值得注意的是，Indomethacin 本身在臨床上已用於 OA 的止痛與抗炎治療，而 Acemetacin 作為其前驅藥，設計目標即在維持等效療效的同時降低直接的胃腸道刺激性。因此 TxGNN 的預測在機轉層面具有合理依據，但 Evidence Pack 中目前缺乏直接支持 Acemetacin 用於骨關節炎的臨床試驗及文獻資料，不足以作為臨床決策依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Acemetacin 目前在香港**未上市**，無相關許可證紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有 TxGNN 模型預測（L5），雖然 COX 抑制機轉與 OA 病理吻合度高，但尚無任何臨床試驗、觀察性研究或文獻直接支持 Acemetacin 用於骨關節炎易感性，且該藥在香港未上市，安全性資料亦存在顯著缺口，無法進入正式評估流程。

**若要推進需要：**
- 補充完整 MOA 資料（優先查詢 DrugBank API，取得 Acemetacin 詳細藥理學資訊）
- 下載原廠仿單 PDF，解析警語、禁忌及藥物交互作用（解除 Blocking Data Gap DG001）
- 以 Indomethacin 在 OA 的臨床證據作為間接佐證，評估前驅藥轉換後的療效等效性
- 確認其他國家/地區（如歐洲、日本）的上市狀態與核准適應症範圍
- 若認為值得深入研究，設計 Acemetacin 對比現有 OA NSAID 療法的探索性 Phase 2 試驗方案
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

