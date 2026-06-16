---
layout: default
title: Felbinac
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 5
---

# Felbinac
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Felbinac：從消炎止痛到短椎-牙釉質發育不全症候群

## 一句話總結

Felbinac 是一種非類固醇消炎止痛藥（NSAID），透過抑制環氧化酶（COX）來減少前列腺素合成，主要用於肌肉骨骼疼痛的消炎止痛。
TxGNN 模型預測它可能對**短椎-牙釉質發育不全症候群（Brachyolmia-Amelogenesis Imperfecta Syndrome）** 有效，
目前**無**臨床試驗或文獻佐證，屬純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 消炎止痛（原適應症資料缺失，依已知藥理推斷） |
| 預測新適應症 | 短椎-牙釉質發育不全症候群（Brachyolmia-Amelogenesis Imperfecta Syndrome） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口）。根據已知資訊，Felbinac（4-聯苯乙酸）是 NSAID 類藥物，透過抑制 COX 酶阻斷前列腺素 E2（PGE2）的合成，在骨代謝與炎症調節中扮演間接角色。

短椎-牙釉質發育不全症候群（Brachyolmia-Amelogenesis Imperfecta Syndrome）是一種極罕見的遺傳性複合症候群，合併全脊椎扁平（短椎症）與牙釉質發育不全，已知致病基因包含 TRPV4（鈣離子通道）及 PAPSS2（硫酸化路徑）。COX 抑制與上述致病路徑**無直接功能連結**，PGE2 調節對骨代謝的影響屬間接推論。

TxGNN 的高分（99.99%）最可能反映知識圖譜中「骨骼發育不全 ↔ 炎症調節」的一般性邊，而非疾病特異性訊號。此預測的機轉合理性極弱，屬推論層次最低的間接推斷，不宜作為優先研究方向。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
所有預測適應症（共 5 項）均為 L5 等級，僅有模型預測，完全無臨床試驗或文獻佐證；機轉連結極為薄弱，且 Felbinac 在香港並無上市許可，現階段不具備推進條件。

**若要重新評估需要：**
- 補充 Felbinac 的作用機轉資料（MOA）及 DrugBank 完整藥理分類
- 確認 Felbinac 是否有任何體外或動物模型研究指向骨骼或結締組織疾病
- 若有興趣探索 NSAID 類藥物在罕見骨骼疾病的角色，建議改以文獻較豐富的 NSAID（如 Celecoxib）作為先導候選，再類推回 Felbinac
- 本候選建議暫緩，待同類藥物有更明確證據後再行評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

