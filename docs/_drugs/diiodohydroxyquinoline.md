---
layout: default
title: Diiodohydroxyquinoline
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Diiodohydroxyquinoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Diiodohydroxyquinoline：從腸道阿米巴病到放射性骨壞死

## 一句話總結

Diiodohydroxyquinoline 是一種鹵化羥基喹啉類抗阿米巴藥，歷史上用於治療**腸道阿米巴病 (Intestinal Amebiasis)**。
TxGNN 模型預測它可能對**放射性骨壞死 (Osteoradionecrosis)** 有效，預測分數高達 97.96%，
然而目前**無臨床試驗亦無相關文獻**直接支持此方向，屬純模型預測（L5 等級），建議暫緩。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腸道阿米巴病（Intestinal Amebiasis，歷史適應症，非本地核准） |
| 預測新適應症 | 放射性骨壞死 (Osteoradionecrosis) |
| TxGNN 預測分數 | 97.96% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據證據包中的已知資訊，Diiodohydroxyquinoline 屬於鹵化羥基喹啉類藥物，具抗原蟲（主要針對腸道阿米巴）及輕度抗菌活性，傳統劑型以**口服腸腔局部作用**為主。

放射性骨壞死是放射治療後因缺血性骨組織損傷引發的嚴重併發症，常伴隨繼發性細菌感染。本藥的抗菌特性，理論上對繼發感染可能有間接關聯，但作用部位限於腸腔，全身性或局部應用於骨組織缺乏充分的藥理學基礎。

**本預測的機轉合理性存疑**：TxGNN 的高分極可能反映知識圖譜中「放射損傷 → 繼發感染 → 抗菌藥物」的共享拓撲結構，而非真實的治療機轉推論。目前無任何臨床試驗或文獻直接研究本藥用於放射性骨壞死，高分數屬圖結構人工訊號的可能性高。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

> ⚠️ **重要安全警示（藥物類別風險）**：Diiodohydroxyquinoline 屬於鹵化羥基喹啉類藥物，同類藥物（如 Clioquinol）已記錄與**亞急性脊髓視神經病變（SMON, Subacute Myelo-Optic Neuropathy）**相關，為嚴重神經毒性，日本曾因此發生大規模用藥事件。此外，鹵化羥基喹啉類藥物可能干擾粒線體功能，對粒線體疾病患者具潛在禁忌風險，使用前應審慎評估。

其他詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測適應症（放射性骨壞死）與本藥的已知作用部位及機轉（腸腔局部抗原蟲）缺乏直接藥理連結，且高分數疑為知識圖譜拓撲人工訊號
- 同類藥物存在 SMON 嚴重神經毒性疑慮、粒線體毒性風險，安全性門檻高，且本藥在香港尚未取得任何上市許可
- 目前無任何臨床試驗或文獻支持此預測，僅為 L5 等級，不具備推進條件

**若要推進需要：**
- 取得完整作用機轉資料（MOA）及原廠仿單安全性資訊
- 系統性評估 SMON 及粒線體毒性與本藥的關聯程度，確認藥物類別是否仍具開發可行性
- 開展前臨床機轉研究，確立本藥對放射性骨組織損傷的直接作用路徑
- 評估給藥途徑相容性——本藥為口服腸腔局部劑型，與骨組織標靶存在根本性不相容問題
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

