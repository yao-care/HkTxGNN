---
layout: default
title: Naphazoline
parent: 僅模型預測 (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Naphazoline：預測新適應症為頭皮單純性毛髮稀疏 (hypotrichosis simplex of the scalp)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Naphazoline"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Naphazoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Naphazoline：從鼻眼充血緩解到頭皮毛髮稀疏（hypotrichosis simplex of the scalp）
{: .text-alpha }

## 一句話總結

Naphazoline 是一種外用的 α 腎上腺素受體促效劑（血管收縮劑），在香港以眼藥水、滴鼻劑和鼻噴霧劑的形式上市，用於緩解眼睛和鼻腔充血。
TxGNN 模型預測它可能對**頭皮單純性毛髮稀疏 (hypotrichosis simplex of the scalp)** 有效，但目前**沒有任何臨床試驗或相關文獻**支持，僅有模型預測，建議暫緩（Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（香港許可證未提供核准適應症文字；依藥理資料，臨床用途為減輕眼睛紅腫充血） |
| 預測新適應症 | 頭皮單純性毛髮稀疏 (hypotrichosis simplex of the scalp) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理資料，Naphazoline 是 α1A、α2A、α2C 腎上腺素受體的配體，透過收縮血管來減輕眼部和鼻腔的充血與紅腫。

**這個預測在機轉上並不合理。** 頭皮單純性毛髮稀疏是遺傳性的毛髮生長疾病，血管收縮並非可信的治療機轉，收縮頭皮血管甚至可能降低毛囊的血流灌注，反而不利於毛髮生長。臨床上與毛髮再生相關的血管作用藥物屬於血管擴張劑（如 minoxidil），而非血管收縮劑。

高分很可能只是知識圖譜中的關聯所致，並非真正的藥理關係。其他排名前列的預測（先天性毛髮稀疏伴粟丘疹、圓形禿、禿髮、多毛症等）同樣沒有機轉依據或臨床資料。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（排名第 8 的預測「開角型青光眼」雖檢索到 1 篇文獻，即 PMID 1295525，但該研究探討的是局部皮質類固醇對雷射誘發周邊前粘連的影響，並未評估 Naphazoline，不能作為證據。）

---

## 香港上市資訊

目前共有 20 張有效的單一成分許可證，皆未提供劑型與核准適應症文字。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42149 | DROPNALIN EYE DROPS 0.1% | 未提供 | 未提供 |
| HK-64948 | ROHTO LYCEE EYE DROPS 0.012% | 未提供 | 未提供 |
| HK-54157 | RINO-NAFTAZOLINA NASAL SPRAY 0.2% | 未提供 | 未提供 |
| HK-17005 | NAPHCON-A OPHTH SOLN | 未提供 | 未提供 |
| HK-01641 | NAPHAZOLINE EYE/NOSE DROPS 0.05% | 未提供 | 未提供 |

從品名可知，產品涵蓋眼藥水、滴鼻劑與鼻噴霧劑。

---

## 安全性考量

- **禁忌症／需謹慎的疾病（來自知識圖譜的藥物－疾病禁忌關聯，非仿單內容）**：高血壓、高血糖、糖尿病、糖尿病酮酸中毒、閉角型青光眼（angle-closure glaucoma）、心血管疾病、心臟病、甲狀腺機能亢進、葛瑞夫茲氏症（Graves disease）、甲狀腺毒症、眼部感染性疾病、結膜炎。
- **作用標的**：α1A、α2A、α2C 腎上腺素受體（人類），另有小鼠 TAAR4 的藥理關聯。上述為受體標的資料，並非具體的藥物交互作用，未提供具體的交互作用藥物清單。
- **青光眼風險**：擬交感神經藥物可能造成瞳孔放大並增加隅角閉鎖風險。若考慮用於青光眼相關適應症，須特別留意。

仿單警語與禁忌的完整內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自圖譜模型（L5），沒有臨床試驗或文獻，且血管收縮劑用於毛髮生長缺乏合理機轉，甚至可能適得其反。
- 排名前 10 的預測皆無實際研究支持；青光眼相關預測還有明確的安全疑慮。

**若要推進需要：**
- 取得 DrugBank 的詳細作用機轉資料，並重新評估機轉關聯。
- 取得香港衛生署仿單（警語、禁忌），補齊安全性資料。
- 先做前臨床（毛囊模型、局部給藥）研究，確認是否有任何生物學合理性，再考慮臨床試驗。
- 確認給藥途徑與劑型是否適合頭皮局部使用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

