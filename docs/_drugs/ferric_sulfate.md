---
layout: default
title: Ferric Sulfate
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 10
---

# Ferric Sulfate
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

# Ferric Sulfate：從牙科局部止血到支氣管炎

## 一句話總結

Ferric sulfate（硫酸鐵）是一種牙科常用的局部止血劑，主要用於組織收縮程序和牙髓切斷術中的傷口止血。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，
但目前僅有 **2 個相關性低的臨床試驗**，且**無任何文獻**直接支持此預測方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 牙科局部止血（組織收縮、牙髓切斷術） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 97.65% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ferric sulfate 是一種局部止血製劑，三價鐵離子（Fe³⁺）與組織蛋白質結合後形成凝塊，達到收斂與止血效果，在牙科操作中廣泛應用。其臨床定位為局部外用藥，全身吸收極為有限。

TxGNN 模型給出 97.65% 的高分，推論機轉可能來自知識圖譜中「鐵代謝 → 先天免疫 → 呼吸道感染」的間接路徑：缺鐵性貧血確實可損害免疫功能，進而影響呼吸道感染的恢復。然而此推論方向存在根本性問題——即便此路徑成立，治療目標應是補充可口服吸收的二價鐵（ferrous salt），而非局部止血用的三價硫酸鐵。

更關鍵的是，現有 2 個臨床試驗所使用的化合物為 sodium ferric gluconate（Ferrlecit®），並非 ferric sulfate，試驗適應症亦為慢性腎臟病缺鐵性貧血，與支氣管炎完全無關。知識圖譜高分可能反映的是圖譜中化合物間接邊的路徑噪音，而非真實的治療機轉連結。

---

## 臨床試驗證據

> ⚠️ 下表試驗與「Ferric sulfate 治療支氣管炎」的關聯性均為 **Grade C（低度相關）**：化合物不符（Ferrlecit® ≠ ferric sulfate），適應症不符（缺鐵性貧血 ≠ 支氣管炎）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00224055](https://clinicaltrials.gov/study/NCT00224055) | Phase 4 | 完成 | 89 | 比較 Ferrlecit®（靜脈鐵劑）與口服亞鐵鹽在**未接受 EPO 治療**的慢性腎臟病缺鐵性貧血患者中的療效，與支氣管炎無直接關聯。 |
| [NCT00224042](https://clinicaltrials.gov/study/NCT00224042) | Phase 4 | 完成 | 52 | 比較 Ferrlecit® 與口服亞鐵鹽在**接受 EPO 治療**的慢性腎臟病缺鐵性貧血患者中的療效，與支氣管炎無直接關聯。 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Ferric sulfate 目前**未在香港取得藥物許可證**，無已核准製劑紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
全部 10 個預測適應症均僅有模型預測（L5），缺乏任何直接臨床或文獻證據；現有 2 個臨床試驗化合物不符且與預測適應症無關。Ferric sulfate 本身為局部外用止血劑，無全身性藥理機轉，使絕大多數預測在臨床轉化上缺乏可行性基礎。部分預測（如 gastroduodenitis、peptic ulcer disease）甚至可能代表模型對「關聯性」與「治療性」區分不足，臨床方向應為禁忌而非適應症。

**若要推進需要：**
- 補充 Ferric sulfate 完整作用機轉（MOA）及全身吸收藥動學資料
- 取得香港衛生署核准仿單，填補警語與禁忌症的 Data Gap
- 針對 Rank 1（支氣管炎）進行深度文獻搜索，確認是否有基礎研究直接支持鐵代謝與支氣管炎的治療關聯
- 評估知識圖譜是否存在逆向因果偏誤（如 Rank 3、4 之胃腸道適應症）
- 若有再利用意向，建議轉換評估對象至系統性吸收鐵劑（如 ferric carboxymaltose），而非局部止血用途之 ferric sulfate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

