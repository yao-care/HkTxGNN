---
layout: default
title: Sevoflurane
parent: 僅模型預測 (L5)
nav_order: 684
evidence_level: L5
indication_count: 5
---

# Sevoflurane
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

# Sevoflurane：從全身麻醉到 5 項候選適應症（Prinzmetal 心絞痛、妥瑞氏症等）

## 一句話總結

Sevoflurane 是臨床廣泛使用的吸入性全身麻醉劑，本評估中**沒有香港許可證資料、無 MOA 記錄**。
TxGNN 模型對其提出 5 項候選新適應症（Prinzmetal angina、Tourette syndrome、fibromyalgia、tendinitis、myositis fibrosa），
但**所有候選的機轉關聯性評估均為「弱」或「不相關」**，僅 2 項候選有文獻但屬麻醉情境共現而非治療證據，
目前**無任何候選達到可進入下一階段審查的證據門檻**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 全身麻醉（誘導與維持）※本 Evidence Pack 未提供許可證/原適應症資料，此為藥物公開已知用途 |
| 預測新適應症（最高分） | Prinzmetal angina（變異型心絞痛） |
| TxGNN 預測分數（最高） | 99.78%（rank 4938） |
| 證據等級 | L5（全部 5 項候選） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | **Hold**（全部候選） |

### 預測候選一覽

| 排名 | 候選適應症 | TxGNN 分數 | 文獻數 | 臨床試驗數 | 決策階段 | 建議 |
|------|-----------|-----------|--------|-----------|---------|------|
| 1 | Prinzmetal angina | 99.78% | 0 | 0 | S0 | Hold |
| 2 | Tourette syndrome | 99.50% | 0 | 0 | S0 | Hold |
| 3 | Fibromyalgia | 99.42% | 1 | 0 | S0 | Hold |
| 4 | Tendinitis | 99.41% | 11 | 0 | S0 | Hold |
| 5 | Myositis fibrosa | 99.41% | 0 | 0 | S0 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Sevoflurane 的詳細作用機轉（MOA）資料，也沒有取得原適應症的完整記錄。根據公開藥理知識，
Sevoflurane 作為吸入性麻醉劑，主要透過調節 **GABA-A 受體**與抑制 **NMDA 受體**產生中樞抑制作用以達成麻醉。

然而，本 Evidence Pack 中**每一項候選適應症的機轉關聯性分析都明確指出關聯性薄弱或不存在**：

- **Prinzmetal angina**：與冠狀動脈痙攣的血管平滑肌調控路徑無明確藥理關聯。
- **Tourette syndrome**：與基底核多巴胺調節機轉無直接對應。
- **Fibromyalgia**：唯一文獻是纖維肌痛症患者接受手術時的「麻醉管理」個案報告，探討的是麻醉安全性，而非 sevoflurane 對該疾病的治療效果。
- **Tendinitis**：11 篇文獻全部是骨科／肌腱手術中使用 sevoflurane 作為麻醉劑的圍術期研究（如旋轉肌袖修復、麻醉深度比較），屬於「手術時剛好用了這個麻醉藥」的情境共現，非治療性證據。
- **Myositis fibrosa**：無任何文獻或試驗，且惡性高熱等肌肉相關風險屬於**禁忌考量**，而非治療機轉。

換言之，TxGNN 的高分很可能反映的是「Sevoflurane 經常出現在這些疾病患者的手術麻醉紀錄中」這種**知識圖譜共現模式**，而非真正的治療潛力訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記（5 項候選適應症皆無 clinical_trials 或 ictrp_trials 記錄）。

---

## 文獻證據

僅 Fibromyalgia、Tendinitis 兩項候選有文獻，且性質均為「圍術期麻醉情境」而非治療證據：

| PMID | 對應候選適應症 | 年份 | 類型 | 期刊 | 主要發現 |
|------|--------------|-----|------|------|---------|
| [26419112](https://pubmed.ncbi.nlm.nih.gov/26419112/) | Fibromyalgia | 2015 | Case Report | Masui | 纖維肌痛症患者接受扁桃腺切除術，以 sevoflurane-remifentanil-fentanyl 麻醉的個案報告，重點為麻醉管理而非治療效果 |
| [38233786](https://pubmed.ncbi.nlm.nih.gov/38233786/) | Tendinitis | 2024 | RCT (麻醉比較) | BMC Anesthesiology | 比較 propofol 與 sevoflurane 對肩關節鏡旋轉肌袖修復手術視野的影響 |
| [34967805](https://pubmed.ncbi.nlm.nih.gov/34967805/) | Tendinitis | 2022 | RCT (麻醉需求) | J Pediatr Orthop | 局部麻醉注射時機對兒童板機指手術吸入性麻醉需求量的影響 |
| [23232381](https://pubmed.ncbi.nlm.nih.gov/23232381/) | Tendinitis | 2013 | Cohort (鎮靜) | J Pediatr Orthop | Propofol 鎮靜用於嬰兒經皮跟腱切開術 |
| [14698365](https://pubmed.ncbi.nlm.nih.gov/14698365/) | Tendinitis | 2003 | RCT (術後鎮痛) | J Clin Anesth | Droperidol 對旋轉肌袖修復術後嗎啡鎮痛效果的影響 |
| [19921357](https://pubmed.ncbi.nlm.nih.gov/19921357/) | Tendinitis | 2009 | RCT (術後鎮痛) | J Anesth | 術前靜脈 flurbiprofen 對肩關節鏡旋轉肌袖修復術後鎮痛的效果 |
| [21299684](https://pubmed.ncbi.nlm.nih.gov/21299684/) | Tendinitis | 2011 | RCT (麻醉需求) | Paediatr Anaesth | 骶管阻滯對腦性麻痺兒童下肢手術 sevoflurane 需求量的影響 |
| [23158561](https://pubmed.ncbi.nlm.nih.gov/23158561/) | Tendinitis | 2012 | RCT (麻醉比較) | Zhonghua Yi Xue Za Zhi | 持續斜角肌間臂叢神經阻滯合併全身麻醉 vs 單純全身麻醉於肩關節鏡手術 |
| [13677277](https://pubmed.ncbi.nlm.nih.gov/13677277/) | Tendinitis | 2003 | Case Report | Masui | Marshall-Smith 症候群病童接受肌腱手術之困難氣道麻醉個案 |
| [20962654](https://pubmed.ncbi.nlm.nih.gov/20962654/) | Tendinitis | 2011 | Case Report | Eur J Anaesthesiol | Sevoflurane 用於甲基丙二酸血症患者之麻醉管理 |

（另有 1 篇 tendinitis 相關文獻 PMID 11212406 因摘要缺失未列出）

**Prinzmetal angina、Tourette syndrome、Myositis fibrosa** 目前無相關文獻。

---

## 香港上市資訊

Sevoflurane 目前**未於香港上市**，無許可證核准紀錄可供列出。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本 Evidence Pack 中主要警語、禁忌症、藥物交互作用均為資料缺口，且列為 **Blocking** 等級 — 無法進行 S1 安全性初評）

---

## 結論與下一步

**決策：Hold（全部 5 項候選適應症）**

**理由：**
- 所有候選的證據等級均為 **L5**（僅模型預測分數，無實質治療性臨床或前臨床證據）。
- 各候選的 `repurposing_rationale` 已明確指出機轉關聯薄弱或不存在，現有文獻多屬「手術麻醉情境共現」而非治療證據。
- 存在 **Blocking 等級資料缺口**（TFDA/仿單警語與禁忌症未取得），無法進行基本安全性初評。
- 香港無上市紀錄，缺乏原適應症與 MOA 基礎資料，無法建立機轉關聯性分析的比較基準。

**若要推進需要：**
- 取得 Sevoflurane 完整仿單警語與禁忌症資料（DG001，Blocking，需下載官方仿單 PDF 解析）
- 取得 DrugBank 完整 MOA 資料（DG002，High，查詢 DrugBank API）
- 針對候選適應症補充真正的治療性臨床試驗或前臨床機轉研究，而非僅圍術期麻醉情境文獻
- 若無法取得上述資料，建議暫停本候選之進一步再利用評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

