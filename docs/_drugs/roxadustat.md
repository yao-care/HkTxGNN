---
layout: default
title: Roxadustat
parent: 僅模型預測 (L5)
nav_order: 790
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Roxadustat：預測新適應症為乾眼症 (Dry Eye Syndrome)（證據等級 L5）。原適應症：難治性貧血 (Refractory Anemia)"
monitor_inn: "ROXADUSTAT"
predicted_indications: ["dry eye syndrome", "bone Paget disease", "dentinogenesis imperfecta", "squamous cell carcinoma"]
---

# Roxadustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Roxadustat：從難治性貧血到乾眼症
{: .text-alpha }

## 一句話總結

Roxadustat 是一種 HIF 脯胺醯羥化酶（HIF-PH）抑制劑，原本用於難治性貧血（在歐洲核准用於慢性腎臟病所致貧血）。
TxGNN 模型預測它可能對**乾眼症 (Dry Eye Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬於模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 難治性貧血 (Refractory Anemia) |
| 預測新適應症 | 乾眼症 (Dry Eye Syndrome) |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理知識，Roxadustat 是 HIF 脯胺醯羥化酶抑制劑，可穩定 HIF-1α/2α，進而促進紅血球生成素的產生，因此用於貧血治療。

HIF 穩定化理論上可能影響角膜與結膜上皮的缺氧反應、發炎與血管新生，這是預測與乾眼症之間可能的連結。但 HIF 活化也可能促進病理性新生血管，對眼表面反而不利。此連結目前屬於推測，99.51% 的分數僅為電腦運算預測。

原適應症（貧血）與乾眼症在疾病性質上差異大，相似度分析尚待進行。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68440 | EVRENZO CAPSULES 50MG | 未提供 | 未提供 |
| HK-68439 | EVRENZO CAPSULES 20MG | 未提供 | 未提供 |

兩張許可證均為單方製劑，狀態有效，持有者為 FIBROGEN INTERNATIONAL (HONG KONG) LIMITED。

---

## 安全性考量

- **藥物交互作用**：藥理資料庫顯示 roxadustat 作用於 EGLN2（egl-9 家族 HIF 2），即其 HIF-PH 抑制的標的，屬藥理作用靶點，並非臨床上的藥物交互作用，也沒有分級資料。
- **其他預測適應症的注意事項**：HIF 穩定化與腫瘤進展、血管新生相關，若未來考慮用於腫瘤相關適應症（如鱗狀細胞癌）須特別謹慎。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有臨床試驗或文獻佐證，且機轉連結屬推測。
- HIF 活化可能促進病理性新生血管，對眼表面的安全性尚不明確。

**若要推進需要：**
- 取得香港衛生署核准仿單，確認警語、禁忌症與核准適應症
- 補充完整的作用機轉資料
- 進行乾眼症相關的文獻回顧與前臨床研究（眼表缺氧、發炎與新生血管模型）
- 評估給藥途徑的可行性（目前僅有口服膠囊，眼科應用可能需要局部劑型）
- 評估 HIF 穩定化的全身性與眼部安全性風險

---

### 其他預測適應症（供參考）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 2 | 骨 Paget 氏病 (Bone Paget Disease) | 99.12% | L5 | Hold |
| 3 | 牙本質發育不全 (Dentinogenesis Imperfecta) | 99.06% | L5 | Hold |
| 4 | 鱗狀細胞癌 (Squamous Cell Carcinoma) | 99.02% | L5 | Hold |

以上三項同樣沒有臨床試驗或文獻支持，機轉連結薄弱。其中鱗狀細胞癌因 HIF 穩定化可能促進腫瘤進展，需特別謹慎。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

