---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Diltiazem：預測新適應症為缺血性中風易感性 (obsolete susceptibility to ischemic stroke)（證據等級 L5）。原適應症：高血壓、心房顫動、Prinzmetal 心絞痛、心室心搏過速"
monitor_inn: "Diltiazem"
predicted_indications: ["obsolete susceptibility to ischemic stroke"]
---

# Diltiazem
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

# Diltiazem：從高血壓與心律不整到「缺血性中風易感性（已廢止術語）」

## 一句話總結

Diltiazem 是一種非二氫吡啶類鈣離子通道阻斷劑，原本用於高血壓、心房顫動、Prinzmetal 心絞痛及心室心搏過速。
TxGNN 模型預測它可能對**缺血性中風易感性 (obsolete susceptibility to ischemic stroke)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、心房顫動、Prinzmetal 心絞痛、心室心搏過速（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 缺血性中風易感性 (obsolete susceptibility to ischemic stroke) |
| TxGNN 預測分數 | 99.08% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 16 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Diltiazem 屬於非二氫吡啶類鈣離子通道阻斷劑，其在高血壓與心血管疾病的療效已被廣泛使用。以下推論來自一般藥理知識，並非本報告所整理資料中的證據：阻斷 L-type 鈣離子通道可降低血壓（中風的主要危險因子），也可能減輕血管痙攣及鈣離子介導的缺血性神經損傷。

需要特別留意的是，這個預測疾病在本體論中被標示為「obsolete（已廢止）」，可能對應不到目前明確定義的臨床適應症。因此這個訊號也可能只是反映與高血壓相關的關聯（已涵蓋於現有適應症），而非獨立的中風預防效果。

TxGNN 分數（0.99）屬於計算預測，不等同於臨床證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 16 張有效單方許可證，無已註銷者。以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51489 | HERBESSER R200 CAP 200MG (JAPAN) | 未載明 | 未載明 |
| HK-36361 | HERBESSER 180 SR CAP 180MG | 未載明 | 未載明 |
| HK-35593 | HERBESSER 90 SR CAP | 未載明 | 未載明 |
| HK-35196 | APO-DILTIAZ TAB 30MG | 未載明 | 未載明 |
| HK-65699 | SYN-DILTIAZEM TABLETS 30MG | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病禁忌關聯，非仿單原文），主要包括：
  - 心臟傳導／節律相關：房室傳導阻滯、病竇症候群、Wolff-Parkinson-White 症候群、Lown-Ganong-Levine 症候群、心室心搏過速
  - 心臟結構／血流動力學：主動脈瓣狹窄、肥厚型心肌病變、低血壓、腎動脈阻塞
  - 器官功能：腎臟疾病、肝臟疾病、膽囊疾病
  - 血液相關：嗜中性白血球低下、顆粒球缺乏症
  - 血管水腫（含遺傳性及 RAAS 阻斷劑引起者）
  - 其他：結締組織、骨骼與軟骨疾病
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 重大 (Major)：Loperamide
  - 中度 (Moderate)：Hydrocortisone、Pioglitazone、Bupropion、Aprepitant、Morphine、Acetylsalicylic acid（阿斯匹靈）、Dexamethasone、Canagliflozin，以及多種鈣鹽製劑（如 Calcium carbonate、Calcium chloride）

仿單的警語與禁忌資料尚未取得，其他安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據僅有模型預測（L5），沒有任何臨床試驗或文獻佐證，且預測的疾病術語已被廢止，臨床意義不明。
- 作用機轉與仿單安全性資料皆缺漏，目前無法進行安全性篩選。

**若要推進需要：**
- 將「obsolete susceptibility to ischemic stroke」對應到現行明確的臨床終點（如中風一級預防或預後改善）
- 取得 DrugBank 的作用機轉資料，進行機轉關聯分析
- 下載並解析香港衛生署的仿單（警語與禁忌）
- 系統性檢索 Diltiazem 與中風相關的臨床試驗和文獻
- 釐清此訊號是否只是高血壓適應症的延伸
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

