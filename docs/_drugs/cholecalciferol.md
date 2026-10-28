---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 4
monitor_inn: "cholecalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "renal osteodystrophy", "renal tubular acidosis"]
last_modified_at: 2026-10-23
description: "Cholecalciferol：預測新適應症為Campailla-Martinelli 型肢中段發育不良（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症文字"
---

# Cholecalciferol
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

## 膽鈣化醇（維生素 D3）：從維生素 D 缺乏與骨代謝疾病到 Campailla-Martinelli 型肢中段發育不良
{: .text-alpha }

## 一句話總結

膽鈣化醇（維生素 D3）在知識圖譜中與骨質疏鬆、佝僂病、骨軟化症及維生素 D 缺乏等疾病有關聯記錄。
TxGNN 模型預測它可能對 **Campailla-Martinelli 型肢中段發育不良** 有效，預測分數很高（0.9978）。
但目前**沒有任何臨床試驗或文獻**直接研究這個疾病，證據僅限於模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症文字；知識圖譜記錄的關聯包括骨質疏鬆、佝僂病、骨軟化症、維生素 D 缺乏、副甲狀腺低下（僅為知識圖譜關聯，非核准適應症） |
| 預測新適應症 | Campailla-Martinelli 型肢中段發育不良 |
| TxGNN 預測分數 | 0.9978 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 13 張／共 13 張） |
| 許可證數 | 13 張（有效 13 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般而言，膽鈣化醇是維生素 D 的前驅物，需經肝臟與腎臟轉化為活性型態，才能調節腸道鈣磷吸收與骨礦化。

肢中段發育不良是罕見的遺傳性骨骼發育疾病。目前沒有證據顯示它由維生素 D 缺乏或鈣磷代謝異常所驅動。模型的高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而不是生物學證據，也不是針對此疾病的特定病理路徑。因此，這個預測目前只能視為待驗證的假說，機轉上的連結尚未建立。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

本報告彙整的資料顯示共有 13 張有效許可證。下表僅列出單一成分的主要產品；其餘許可證多為複方或其他用途產品（例如與 alendronate 的複方、綜合維生素、動物用注射劑），不能用來描述單一成分膽鈣化醇的核准狀態，故不列入。各許可證的劑型與核准適應症文字在資料中均為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67080 | VITA GREEN VITAMIN D3 TABLETS 1200IU | VITA GREEN PHARMACEUTICAL (H.K.) LIMITED |
| HK-68740 | DECUROL CAPSULES 25000IU | GALEPHAR HK LIMITED |
| HK-68743 | DECUROL ORAL DROPS 2400IU/ML | GALEPHAR HK LIMITED |
| HK-68742 | DECUROL ORAL SOLUTION 25000IU/1ML | GALEPHAR HK LIMITED |
| HK-68741 | DECUROL ORAL SOLUTION 100000IU/1ML | GALEPHAR HK LIMITED |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：包括高血鈣相關疾病（高副甲狀腺機能亢進、高血鈣、腎鈣質沉著症、磷代謝疾病）、肉芽腫性疾病（類肉瘤病）、腎臟與肝臟疾病、高血壓、糖尿病、心房顫動、原發性高草酸尿症、血色素沉著症、威爾森氏症、高血脂，以及乳癌與攝護腺癌等。
- **藥物交互作用**：資料庫共記錄 56 筆，以下為已列出的主要項目。
  - 嚴重（Major）：Calcifediol、Calcitriol、Dihydrotachysterol、Doxercalciferol（皆為其他維生素 D 類，合用有高血鈣風險）
  - 中度（Moderate）：thiazide 類利尿劑（Bendroflumethiazide、Chlorothiazide、Chlorthalidone 等）、巴比妥類（Amobarbital、Butabarbital、Butalbital）、Carbamazepine、膽酸結合劑（Cholestyramine、Colesevelam、Colestipol）、強心苷（Digoxin、Digitoxin）
  - 輕微（Minor）：Cimetidine

仿單的警語與禁忌資料未能取得，完整安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測只有模型分數，沒有任何臨床試驗或文獻直接研究該疾病，證據等級為 L5。
- 機轉上也沒有疾病特異性的連結，目前不宜推進。

**若要推進需要：**
- 找出肢中段發育不良與維生素 D 或鈣磷代謝路徑的具體病理關聯（如基因與路徑層級的分析）
- 補充膽鈣化醇的作用機轉資料與香港仿單的警語及禁忌內容
- 先進行系統性文獻回顧或個案資料蒐集，確認是否有任何臨床訊號

**補充：同一份預測清單中的其他候選**
- 腎性骨失養症排名第 3，預測分數 0.9911，已有一項 Phase 3 試驗（NCT00752401，腎移植受者，狀態未知、無結果）、一項已完成的小型試驗（NCT00285467）及多篇文獻。
- 資料中該項標示為 L1 及 Proceed with Guardrails，但該 Phase 3 試驗的族群與狀態存在限制，分級仍屬暫定。
- 若以實際可推進性考量，這個候選比排名第 1 的疾病更值得優先評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

