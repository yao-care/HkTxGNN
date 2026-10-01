---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide：從既有上市適應症到異位性濕疹

## 一句話總結

Budesonide 是一種糖皮質素（glucocorticoid），已在香港以多種產品上市，但目前資料中沒有可引用的核准適應症文字。
TxGNN 模型預測它可能對**異位性濕疹 (Atopic Eczema)** 有效，預測分數很高。
目前有 **2 個臨床試驗**和 **20 篇文獻**與此方向相關，但沒有任何一項直接證明 budesonide 治療濕疹有效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 異位性濕疹 (Atopic Eczema) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L4（僅有前臨床配方研究與類別機轉推論） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。根據已知資訊，budesonide 屬於糖皮質素類藥物，其抗發炎作用在多種發炎性疾病中已被廣泛使用。外用皮質類固醇本來就是異位性皮膚炎的標準藥物類別，所以機轉上可能適用於濕疹。

TxGNN 的高分（99.96%）很可能反映的是這個「類別效應」，而不是 budesonide 本身的專屬證據。

需要注意的是，目前沒有找到 budesonide 治療濕疹的臨床療效資料。唯一與皮膚劑型相關的是 2024 年的前臨床奈米粒子水凝膠研究。多篇文獻反而報告了 budesonide 的接觸性過敏，這是一個安全性警訊。

「dermatitis, atopic」（排名 3）與本項是同一疾病的重複條目，證據內容相同，已合併處理。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | 完成 | 58 | 過敏原免疫療法用於預防異位性喘鳴幼童的氣喘。濕疹只是受試者的過敏背景，並未測試 budesonide |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | 不適用（觀察性） | 未知 | 150 | 重度兒童氣喘的內生型（endotype）特徵分析，並未測試 budesonide 治療濕疹 |

兩個試驗與本適應症的相關性都被評為 C 級（低度相關）。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | 隨機對照試驗（犬隻） | J Vet Pharmacol Ther | 0.025% budesonide 護毛劑可改善犬異位性皮膚炎的皮膚病灶與搔癢。此為獸醫研究，不能直接類推人類 |
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | 前臨床配方研究 | Gels | 將 budesonide 載入 pH 敏感奈米粒子水凝膠，用於異位性皮膚炎局部治療，尚無臨床資料 |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | 開放式縱向試驗 | Pediatr Dermatol | 14 名 5–12 歲異位性皮膚炎兒童，以測腿儀評估外用 budesonide 對短期生長的影響 |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | 臨床研究 | Dermatology | 外用糖皮質素可經皮吸收，可能抑制兒童生長，研究其對 IGF 軸與骨、膠原代謝的影響 |
| [35184304](https://pubmed.ncbi.nlm.nih.gov/35184304/) | 2022 | 病例報告 | Contact Dermatitis | budesonide 斑貼試驗後出現全身性過敏性皮膚炎 |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | 斑貼試驗 | Contact Dermatitis | 義大利 SIDAPA 基準系列中的 budesonide 斑貼試驗。budesonide 是皮質類固醇過敏的標記物，近二十年過敏率呈下降趨勢 |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | 橫斷面研究 | Contact Dermatitis | 亞洲皮膚科中心比較有無異位性皮膚炎患者的接觸致敏模式 |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | 橫斷面研究 | Dermatitis | 異位性皮膚炎青少年與成人對歐洲標準系列及皮質類固醇系列半抗原的接觸過敏 |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | 研究 | Allergy | 氣喘患者中糖皮質素過敏的發生情形 |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | 病例報告 | Cureus | 一名有異位性皮膚炎病史的患者，因類固醇出現第一型過敏反應（血管性水腫與蕁麻疹） |

## 香港上市資訊

資料中 20 張許可證的劑型與核准適應症欄位皆為空白，以下僅列出前 5 張：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68212 | NEFECON MODIFIED-RELEASE CAPSULES 4MG | EVEREST MEDICINES II (HK) LIMITED |
| HK-60236 | BIOSONIDE NASAL SPRAY 100MCG/DOSE | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-64964 | CORTIMENT PROLONGED RELEASE TABLETS 9 MG | FERRING PHARMACEUTICALS LTD |
| HK-51729 | BUDESONIDE PH&T 50 NASAL SPRAY 50MCG/DOSE | HONG KONG MEDICAL SUPPLIES LTD |
| HK-64327 | BUDENA NASAL SPRAY 64 MCG/SPRAY | MEKIM LTD |

從品名判斷，這 5 張都是鼻噴劑或口服緩釋劑型，未見皮膚外用劑型。

## 安全性考量

安全性資訊請參考原廠仿單。目前尚未取得香港衛生署仿單的警語與禁忌資料，DrugBank 也查無藥物交互作用紀錄。

文獻中出現的訊號：
- **接觸致敏**：多篇報告指出 budesonide 可引起接觸性過敏，甚至全身性過敏反應。異位性皮膚炎患者的皮膚屏障受損，值得特別留意。
- **兒童生長**：外用糖皮質素可經皮吸收，可能影響兒童生長。

## 結論與下一步

**決策：Hold**

**理由：**
- 高預測分數主要來自糖皮質素的類別效應，缺乏 budesonide 專屬的臨床證據。
- 唯一的皮膚劑型研究仍在前臨床階段，且文獻中有多項接觸過敏的安全性警訊。
- 目前的證據等級為 L4。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌（此缺口目前阻擋安全性篩選）。
- 補齊 budesonide 的作用機轉資料。
- 確認是否有適合皮膚使用的劑型與給藥途徑（已列出的香港產品中未見外用劑型）。
- 找到 budesonide 與現有外用類固醇在異位性皮膚炎的head-to-head 臨床證據，並評估接觸致敏風險。

**其他預測適應症：** 「支氣管炎」（排名 2）的證據較多（L3，「研究問題」層級），但需先界定具體亞型（如嗜酸性或慢性支氣管炎）。若要優先評估，可考慮以該項為起點。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

