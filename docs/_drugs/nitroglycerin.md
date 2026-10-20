---
layout: default
title: Nitroglycerin
parent: 中證據等級 (L3-L4)
nav_order: 625
evidence_level: L3
indication_count: 5
last_modified_at: 2026-10-14
description: "Nitroglycerin：預測新適應症為肺動脈高壓 (Pulmonary Hypertension)（證據等級 L3）。原適應症：香港許可證資料未載明核准適應症"
monitor_inn: "nitroglycerin"
predicted_indications: ["pulmonary hypertension", "kyphoscoliotic heart disease", "primary hereditary glaucoma", "congenital hypotrichosis milia"]
---

# Nitroglycerin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Nitroglycerin：從心絞痛類適應症到肺動脈高壓

## 一句話總結

Nitroglycerin（硝酸甘油）是一種有機硝酸鹽血管擴張劑，在香港有舌下錠、噴劑、注射劑及穿皮貼片等多種劑型上市。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，
目前有 **3 個臨床試驗**和 **20 篇文獻**支持這個方向，但多為小型血行動力學研究、兒童與新生兒研究及圍手術期研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症 |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.61% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏經資料庫確認的詳細作用機轉資料。就藥理常識而言，硝酸甘油是有機硝酸鹽，會釋放一氧化氮 (NO)，活化可溶性鳥苷酸環化酶 (sGC) 並提高血管平滑肌內的 cGMP，進而造成血管擴張。

肺動脈高壓的核心問題是肺血管持續收縮與血管重塑。NO-cGMP 路徑正是吸入性一氧化氮及 PDE5 抑制劑用於肺動脈高壓的機轉，因此在生物學上有合理性。霧化或吸入給藥可能帶來相對的肺部選擇性，並減少全身性低血壓。

需注意的限制：可能造成通氣灌流 (V/Q) 不匹配，以及全身性低血壓風險。目前證據主要來自小型血行動力學研究、兒童/新生兒研究和圍手術期研究，而非 Phase 3 RCT。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07214129](https://clinicaltrials.gov/study/NCT07214129) | 未分期 (NA) | 完成 | 20 | 霧化硝酸甘油作為肺動脈高壓血管反應性測試藥物的安全性與療效 |
| [NCT04594629](https://clinicaltrials.gov/study/NCT04594629) | Phase 1 | 狀態未知 | 120 | 瓣膜置換術後肺高壓：霧化 PGI2 與霧化硝酸甘油比較（隨機分組） |
| [NCT07603037](https://clinicaltrials.gov/study/NCT07603037) | 未分期 (NA) | 尚未招募 | 12 | Nicardipine 與硝酸甘油對急性呼吸衰竭患者通氣灌流比的影響（與肺高壓僅間接相關） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40888971](https://pubmed.ncbi.nlm.nih.gov/40888971/) | 2025 | RCT | Eur J Pediatr | 80 名新生兒持續性肺高壓，霧化硝酸甘油作為輔助治療，評估心臟超音波與臨床指標變化 |
| [29880427](https://pubmed.ncbi.nlm.nih.gov/29880427/) | 2018 | RCT | J Cardiothorac Vasc Anesth | 二尖瓣置換術重度肺高壓：Dobutamine 加硝酸甘油與 Milrinone 比較 |
| [34082850](https://pubmed.ncbi.nlm.nih.gov/34082850/) | 2021 | 臨床研究/回顧 | Cardiol Young | 吸入硝酸甘油用於先天性心臟病兒童急性肺動脈高壓 |
| [16707530](https://pubmed.ncbi.nlm.nih.gov/16707530/) | 2006 | 臨床研究 | Br J Anaesth | 吸入硝酸甘油對先天性心臟病兒童肺與全身血行動力學的急性影響 |
| [6407380](https://pubmed.ncbi.nlm.nih.gov/6407380/) | 1983 | 臨床血行動力學研究 | Ann Intern Med | 9 名慢性肺高壓患者，心輸出指數與每搏量增加約 40%，肺血管阻力降低約 40% |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | 臨床血行動力學研究 | Bull Eur Physiopathol Respir | COPD 肺高壓：硝酸甘油可降低肺動脈壓與肺血管阻力 |
| [3096761](https://pubmed.ncbi.nlm.nih.gov/3096761/) | 1986 | 臨床研究 | Eur J Respir Dis Suppl | 穿皮貼片硝酸甘油使肺動脈壓下降，4 週持續治療後仍可見效果 |
| [8908227](https://pubmed.ncbi.nlm.nih.gov/8908227/) | 1996 | 臨床研究 | Acta Anaesthesiol Scand | 末期心肌病變患者，硝酸甘油與 isosorbide dinitrate 的肺血管效應比較 |
| [42572609](https://pubmed.ncbi.nlm.nih.gov/42572609/) | 2026 | Review | JHLT Open | 圍手術期吸入性肺血管擴張劑的使用與臨床考量 |
| [39059783](https://pubmed.ncbi.nlm.nih.gov/39059783/) | 2024 | Review | Curr Probl Cardiol | 霧化吸入治療肺動脈高壓的進展 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-21410 | NITRODERM TTS 10 10MG/24 HOURS | 未載明（穿皮貼片系列） | 未載明 |
| HK-17865 | NITRODERM TTS 5 5MG/24 HOURS | 未載明（穿皮貼片系列） | 未載明 |
| HK-53929 | GLYCERYL TRINITRATE-HAMELN INJ 1MG/ML | 注射劑 | 未載明 |
| HK-42848 | NITRO POHL FOR INTRAVENOUS INJ 1MG/ML | 注射劑 | 未載明 |
| HK-58236 | GLYCERYL TRINITRATE SOLN FOR INF 1MG/ML | 輸注溶液 | 未載明 |

---

## 安全性考量

- **禁忌症（來自知識圖譜，非仿單文字）**：知識圖譜列出的禁忌相關疾病包括低血壓、肥厚性心肌病變、高鐵血紅蛋白血症、硫血紅蛋白血症、貧血、巨球性貧血、腦內出血、縮窄性心包膜炎、限制型心肌病變及心包填塞。
- **藥物交互作用**：共查得 228 筆。中度交互作用包括 Bupropion、Morphine、Canagliflozin、Dapagliflozin、Empagliflozin、Dronabinol、Nabilone、Rosiglitazone、Sapropterin 等；輕度包括 Atropine、Hyoscyamine、Scopolamine、Acetylsalicylic acid、Omeprazole 等。

其餘警語與仿單資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多項小型血行動力學研究、一項新生兒 RCT 及圍手術期研究支持硝酸甘油（特別是霧化/吸入給藥）降低肺動脈壓與肺血管阻力，機轉上合理。但缺乏 Phase 3 RCT，已登記的試驗也偏小型或早期，證據等級為 L3。
- 全身性低血壓與通氣灌流不匹配的風險須嚴格管控。

**若要推進需要：**
- 取得香港原廠仿單的警語與禁忌資料（目前為重要缺口）
- 補充詳細作用機轉資料
- 設計適當規模的隨機對照試驗，優先評估霧化/吸入劑型與給藥途徑
- 建立血壓與氧合的監測計畫，並避開知識圖譜所列禁忌族群
- 確認香港現有劑型（貼片、注射、舌下錠、噴劑）是否適用於吸入給藥，目前吸入劑型尚無香港許可證

---

### 其他預測適應症（供參考）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 後側彎性心臟病 (Kyphoscoliotic heart disease) | 99.42% | L5 | Hold：僅有模型預測，且可能惡化 V/Q 匹配 |
| 變異型心絞痛 (Prinzmetal angina) | 99.39% | L4 | Research Question：臨床上已屬既有用法，並非典型再利用 |
| 原發性遺傳性青光眼 | 99.16% | L5 | Hold：機轉依據薄弱，無試驗或文獻 |
| 先天性稀毛症伴粟丘疹 | 99.02% | L5 | Hold：無明確機轉連結，不建議推進 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

