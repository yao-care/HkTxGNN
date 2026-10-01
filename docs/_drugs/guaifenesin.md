---
layout: default
title: Guaifenesin
parent: 中證據等級 (L3-L4)
nav_order: 422
evidence_level: L3
indication_count: 5
---

# Guaifenesin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Guaifenesin：從祛痰到鼻腔疾病

## 一句話總結

Guaifenesin 是常見的祛痰劑，透過稀釋黏液、促進痰液排出來緩解呼吸道症狀。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
目前有 **1 個臨床試驗**和 **2 篇文獻**支持這個方向，但證據偏薄弱，僅屬研究假說階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理知識，Guaifenesin 是祛痰劑，被認為能增加呼吸道分泌液體積並降低黏液黏稠度，讓黏液更容易清除。

慢性鼻炎與鼻竇疾病常伴隨黏稠的鼻腔分泌物。若能改善黏液性質，理論上可減輕鼻塞與分泌物滯留等症狀。這個關聯在症狀層面上合理，但並非經過驗證的疾病機轉，只能視為依一般藥理推論的假說。

TxGNN 對其他四項預測（急性喉咽炎、咽白喉、頸椎椎間盤退化、乳突性結膜炎）同樣給出很高分數，但都沒有臨床試驗或文獻支持，屬於 L5 等級，建議暫緩。其中咽白喉與乳突性結膜炎在機轉上缺乏可信的連結，很可能是知識圖譜的關聯假象。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | 完成 | 30 | 口服 Guaifenesin 用於 7–18 歲兒童慢性鼻炎的前導研究，為期 14 天，以安慰劑對照設計，評估鼻部症狀量表 (SN-5)、鼻氣道體積與鼻分泌物的物理性質。目前未提供結果。 |

此試驗樣本小，僅針對兒童，且未公開結果，因此不能推論到成人，也無法確認療效。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9065342](https://pubmed.ncbi.nlm.nih.gov/9065342/) | 1997 | Review | American Journal of Rhinology | 回顧 22 位成人囊性纖維化合併慢性鼻竇炎患者的處置經驗，並提出管理建議。 |
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | 討論嗓音使用者的隱性呼吸道過敏治療策略，指出含 Guaifenesin 的鼻充血緩解劑可能有幫助。 |

兩篇皆為間接相關的回顧，並非針對 Guaifenesin 療效的對照研究。

## 香港上市資訊

香港共有 20 張含 Guaifenesin 的許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62004 | MUCINEX EXTENDED-RELEASE TABLETS 600MG | RECKITT BENCKISER HONG KONG LTD |
| HK-47305 | GUFENSIN TAB 200MG | CHRISTO PHARM LTD |
| HK-40322 | EXCAUGH TAB | FORTUNE PHARMACAL COMPANY LIMITED |
| HK-07378 | GUAIAPHEN SYRUP 100MG/5ML | MARCHING PHARMACEUTICAL LIMITED |
| HK-36928 | BREACOL SYRUP | A. MENARINI HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
目前只有 1 個小型、兒童族群的 Phase 2 前導試驗（未公開結果）和 2 篇間接相關的回顧，證據等級為 L3。香港仿單的警語與禁忌資料也尚未取得，無法進入安全性篩選。機轉僅屬症狀層面的合理推論，因此建議暫列為研究問題，不進一步推進。

**若要推進需要：**
- 取得 NCT01364467 的結果，確認療效訊號與研究設計（是否隨機、有無對照組）
- 補充成人慢性鼻炎或鼻竇疾病的對照試驗證據
- 下載並解析香港衛生署的仿單，補齊警語與禁忌症
- 從 DrugBank 補充作用機轉資料，以便進行機轉關聯分析
- 釐清香港各許可證的核准適應症與劑型

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

